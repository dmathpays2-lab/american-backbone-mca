#!/bin/bash
# Tandem Auto-Restart Monitor
# Checks Tandem every 5 minutes and restarts if dead

TANDEM_DIR="$HOME/tandem-browser"
API_URL="http://127.0.0.1:8765/status"
LOG_FILE="/var/log/tandem-monitor.log"
PID_FILE="/tmp/tandem-monitor.pid"

# Create log directory if needed
mkdir -p "$(dirname "$LOG_FILE")" 2>/dev/null || LOG_FILE="/tmp/tandem-monitor.log"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# Check if already running
if [ -f "$PID_FILE" ]; then
    OLD_PID=$(cat "$PID_FILE" 2>/dev/null)
    if ps -p "$OLD_PID" > /dev/null 2>&1; then
        log "Monitor already running (PID: $OLD_PID)"
        exit 0
    fi
fi

echo $$ > "$PID_FILE"
log "=== Tandem Monitor Started (PID: $$) ==="

# Trap to clean up on exit
trap 'rm -f "$PID_FILE"; log "Monitor stopped"; exit 0' INT TERM EXIT

# Health check function
check_tandem() {
    if curl -s --max-time 10 "$API_URL" > /dev/null 2>&1; then
        return 0  # Healthy
    else
        return 1  # Dead
    fi
}

# Restart function
restart_tandem() {
    log "Tandem not responding - restarting..."
    
    # Kill any existing processes
    pkill -f "electron.*tandem" 2>/dev/null
    pkill -f "Xvfb.*:99" 2>/dev/null
    sleep 3
    
    # Start Xvfb
    export DISPLAY=:99
    Xvfb :99 -screen 0 1280x720x24 -ac &
    sleep 2
    
    # Start Tandem
    cd "$TANDEM_DIR" || exit 1
    nohup ./node_modules/electron/dist/electron . --no-sandbox --disable-gpu > /tmp/tandem.log 2>&1 &
    TANDEM_PID=$!
    echo "$TANDEM_PID" > "$TANDEM_DIR/.tandem.pid"
    
    log "Tandem restarted (PID: $TANDEM_PID)"
    
    # Wait for API to be ready
    for i in {1..30}; do
        if check_tandem; then
            log "Tandem API is ready"
            return 0
        fi
        sleep 2
    done
    
    log "Tandem failed to start within 60 seconds"
    return 1
}

# Main monitoring loop
while true; do
    if ! check_tandem; then
        log "Health check failed"
        restart_tandem
    fi
    
    # Check every 5 minutes
    sleep 300
done
