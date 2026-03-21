#!/usr/bin/env python3
"""
OpenClaw Health Monitor - Prevents IM timeout deaths
Watches for stuck runs and kills them before they hit the timeout wall
"""

import json
import os
import sys
import time
import subprocess
import signal
from datetime import datetime, timedelta
from pathlib import Path

# Config
WORKSPACE = Path("/root/.openclaw/workspace")
LOGS_DIR = Path("/root/.openclaw/logs")
SESSIONS_DIR = Path("/root/.openclaw/agents/main/sessions")
MAX_RUN_MINUTES = 8  # Kill runs approaching 10min limit
ALERT_THRESHOLD_MINUTES = 5  # Log warning at 5min

# Track file for persistence
STATE_FILE = WORKSPACE / ".health_state.json"

def load_state():
    """Load previous run state"""
    if STATE_FILE.exists():
        try:
            with open(STATE_FILE) as f:
                return json.load(f)
        except:
            pass
    return {"last_check": None, "killed_runs": []}

def save_state(state):
    """Save state for next run"""
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2)

def get_running_runs():
    """Get list of currently running OpenClaw runs"""
    runs = []
    try:
        # Check sessions directory for active runs
        if SESSIONS_DIR.exists():
            for session_file in SESSIONS_DIR.glob("*.jsonl"):
                try:
                    stat = session_file.stat()
                    mtime = datetime.fromtimestamp(stat.st_mtime)
                    age_minutes = (datetime.now() - mtime).total_seconds() / 60
                    
                    runs.append({
                        "session": session_file.name,
                        "mtime": mtime.isoformat(),
                        "age_minutes": round(age_minutes, 2),
                        "size_mb": round(stat.st_size / 1024 / 1024, 2)
                    })
                except:
                    pass
    except Exception as e:
        print(f"Error checking sessions: {e}")
    
    return runs

def check_gateway_health():
    """Check if gateway is responsive"""
    try:
        result = subprocess.run(
            ["openclaw", "gateway", "status"],
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.returncode == 0 and "running" in result.stdout
    except:
        return False

def get_recent_timeouts():
    """Check logs for recent timeout errors"""
    timeouts = []
    try:
        log_file = LOGS_DIR / "openclaw.log"
        if log_file.exists():
            # Check last 100 lines for timeout errors
            result = subprocess.run(
                ["tail", "-100", str(log_file)],
                capture_output=True,
                text=True
            )
            for line in result.stdout.split('\n'):
                if 'timed out' in line.lower() or 'dispatch' in line.lower():
                    timeouts.append(line[:200])  # Truncate long lines
    except:
        pass
    return timeouts[-5:]  # Last 5 timeout-related entries

def kill_stuck_runs(runs):
    """Kill runs that are approaching timeout"""
    killed = []
    for run in runs:
        if run["age_minutes"] > MAX_RUN_MINUTES:
            # Try to find and kill the process
            try:
                # Extract session ID from filename
                session_id = run["session"].replace(".jsonl", "")
                
                # Look for node processes with this session
                result = subprocess.run(
                    ["pgrep", "-f", f"{session_id[:8]}"],
                    capture_output=True,
                    text=True
                )
                
                if result.stdout.strip():
                    pid = int(result.stdout.strip().split('\n')[0])
                    os.kill(pid, signal.SIGTERM)
                    time.sleep(2)
                    try:
                        os.kill(pid, signal.SIGKILL)
                    except:
                        pass
                    
                    killed.append({
                        "session": run["session"],
                        "age_minutes": run["age_minutes"],
                        "pid": pid,
                        "killed_at": datetime.now().isoformat()
                    })
                    print(f"☠️  Killed stuck run: {run['session']} (age: {run['age_minutes']:.1f}min)")
                    
            except Exception as e:
                print(f"Failed to kill {run['session']}: {e}")
    
    return killed

def generate_report(runs, timeouts, gateway_ok, killed):
    """Generate health report"""
    report = []
    report.append("═" * 50)
    report.append("🩺 OPENCLAW HEALTH REPORT")
    report.append(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append("═" * 50)
    
    # Gateway status
    status = "✅ RUNNING" if gateway_ok else "❌ DOWN"
    report.append(f"\n🌐 Gateway: {status}")
    
    # Active runs
    report.append(f"\n📊 Active Sessions: {len(runs)}")
    
    long_runs = [r for r in runs if r["age_minutes"] > ALERT_THRESHOLD_MINUTES]
    if long_runs:
        report.append(f"\n⚠️  LONG-RUNNING SESSIONS (>5min):")
        for run in sorted(long_runs, key=lambda x: x["age_minutes"], reverse=True):
            status = "🔴 KILLED" if any(k["session"] == run["session"] for k in killed) else "🟡 WARNING"
            report.append(f"   {status} {run['session'][:20]}... | {run['age_minutes']:.1f}min | {run['size_mb']}MB")
    
    # Killed runs
    if killed:
        report.append(f"\n☠️  KILLED THIS RUN:")
        for k in killed:
            report.append(f"   - {k['session'][:20]}... at {k['age_minutes']:.1f}min")
    
    # Recent timeouts
    if timeouts:
        report.append(f"\n🚨 RECENT TIMEOUTS IN LOGS:")
        for t in timeouts:
            report.append(f"   {t[:80]}...")
    
    report.append("\n" + "═" * 50)
    
    return "\n".join(report)

def main():
    """Main health check routine"""
    state = load_state()
    
    # Get current status
    runs = get_running_runs()
    timeouts = get_recent_timeouts()
    gateway_ok = check_gateway_health()
    
    # Kill stuck runs
    killed = kill_stuck_runs(runs)
    
    # Update state
    if killed:
        state["killed_runs"].extend(killed)
        state["killed_runs"] = state["killed_runs"][-20:]  # Keep last 20
    
    state["last_check"] = datetime.now().isoformat()
    save_state(state)
    
    # Print report
    report = generate_report(runs, timeouts, gateway_ok, killed)
    print(report)
    
    # Exit code indicates health
    if not gateway_ok:
        sys.exit(2)  # Critical
    elif long_runs := [r for r in runs if r["age_minutes"] > ALERT_THRESHOLD_MINUTES]:
        sys.exit(1)  # Warning
    else:
        sys.exit(0)  # Healthy

if __name__ == "__main__":
    main()
