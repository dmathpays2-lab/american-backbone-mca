#!/usr/bin/env python3
"""
Session Freshness Manager
Keeps OpenClaw sessions lean by monitoring and suggesting rotation
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path

SESSION_FILE = Path("/root/.openclaw/workspace/.session_freshness.json")
TRANSCRIPT_DIR = Path("/root/.openclaw/agents/main/sessions")

# Thresholds
MAX_TOKENS = 80000      # Suggest rotation at 80K tokens
MAX_TURNS = 50          # Suggest rotation after 50 turns  
MAX_AGE_HOURS = 4       # Suggest rotation after 4 hours
COMPACT_THRESHOLD = 60000  # Auto-compact at 60K

class SessionFreshnessManager:
    def __init__(self):
        self.state = self.load_state()
        self.session_key = "agent:main:main"
        
    def load_state(self):
        if SESSION_FILE.exists():
            try:
                with open(SESSION_FILE) as f:
                    return json.load(f)
            except:
                pass
        return {
            "session_start": datetime.now().isoformat(),
            "turn_count": 0,
            "last_compact": None,
            "rotations": []
        }
    
    def save_state(self):
        with open(SESSION_FILE, 'w') as f:
            json.dump(self.state, f, indent=2)
    
    def estimate_tokens(self, transcript_path):
        """Rough token estimate from transcript size"""
        try:
            if transcript_path.exists():
                size_bytes = transcript_path.stat().st_size
                # Rough estimate: 1 token ≈ 4 bytes for text
                return size_bytes // 4
        except:
            pass
        return 0
    
    def get_transcript_size_mb(self):
        """Get current session transcript size"""
        try:
            transcript = TRANSCRIPT_DIR / "4bd8faa1-3142-4551-a3b3-0e501acad41e.jsonl"
            if transcript.exists():
                return transcript.stat().st_size / 1024 / 1024
        except:
            pass
        return 0
    
    def get_session_age_hours(self):
        """How long since session started"""
        try:
            start = datetime.fromisoformat(self.state["session_start"])
            return (datetime.now() - start).total_seconds() / 3600
        except:
            return 0
    
    def get_health_score(self):
        """
        Returns 0-100 freshness score
        100 = fresh, 0 = needs rotation
        """
        score = 100
        
        # Token pressure (-20 per 10K over threshold)
        tokens = self.estimate_tokens(TRANSCRIPT_DIR / "4bd8faa1-3142-4551-a3b3-0e501acad41e.jsonl")
        if tokens > MAX_TOKENS:
            score -= min(40, (tokens - MAX_TOKENS) // 10000 * 10)
        
        # Turn count (-10 per 10 turns over)
        turns = self.state.get("turn_count", 0)
        if turns > MAX_TURNS:
            score -= min(30, (turns - MAX_TURNS) // 10 * 10)
        
        # Age (-10 per hour over)
        age = self.get_session_age_hours()
        if age > MAX_AGE_HOURS:
            score -= min(30, (age - MAX_AGE_HOURS) * 5)
        
        return max(0, score)
    
    def record_turn(self):
        """Call this every turn to track"""
        self.state["turn_count"] = self.state.get("turn_count", 0) + 1
        self.save_state()
    
    def record_compact(self):
        """Track when compaction happens"""
        self.state["last_compact"] = datetime.now().isoformat()
        self.save_state()
    
    def suggest_rotation(self):
        """Returns True if we should start fresh"""
        return self.get_health_score() < 50
    
    def generate_report(self):
        """Generate freshness report"""
        score = self.get_health_score()
        tokens = self.estimate_tokens(TRANSCRIPT_DIR / "4bd8faa1-3142-4551-a3b3-0e501acad41e.jsonl")
        turns = self.state.get("turn_count", 0)
        age = self.get_session_age_hours()
        size_mb = self.get_transcript_size_mb()
        
        # Status emoji
        if score >= 80:
            status = "🟢 FRESH"
        elif score >= 50:
            status = "🟡 AGING"
        else:
            status = "🔴 ROTATE"
        
        report = []
        report.append("═" * 45)
        report.append("🔄 SESSION FRESHNESS REPORT")
        report.append("═" * 45)
        report.append(f"Health Score: {score}/100 {status}")
        report.append("")
        report.append(f"📊 Estimated Tokens: {tokens:,}")
        report.append(f"💬 Turn Count: {turns}")
        report.append(f"⏱️  Session Age: {age:.1f} hours")
        report.append(f"📁 Transcript: {size_mb:.1f} MB")
        report.append("")
        
        if score < 50:
            report.append("⚠️  RECOMMENDATION: Start new session")
            report.append("   New sessions clear context bloat,")
            report.append("   stuck subagents, and tool state.")
        elif score < 80:
            report.append("💡 TIP: Approaching rotation threshold")
            report.append("   Consider wrapping up current task")
        else:
            report.append("✅ Session is healthy and fresh")
        
        report.append("═" * 45)
        
        return "\n".join(report), score < 50

def main():
    manager = SessionFreshnessManager()
    report, should_rotate = manager.generate_report()
    print(report)
    return 1 if should_rotate else 0

if __name__ == "__main__":
    exit(main())
