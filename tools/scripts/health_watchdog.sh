#!/bin/bash
# OpenClaw timeout watchdog - kills runs before they die of old age
# Run every 5 minutes via cron

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPORT_FILE="/root/.openclaw/workspace/.health_report.txt"
LOG_FILE="/root/.openclaw/logs/health_watchdog.log"

# Run health check with timeout (prevent hanging)
timeout 25 python3 "$SCRIPT_DIR/health_monitor.py" > "$REPORT_FILE" 2>&1
EXIT_CODE=$?

# Log result quietly
if [ $EXIT_CODE -eq 2 ]; then
    echo "$(date '+%H:%M'): Gateway down, restarting..." >> "$LOG_FILE"
    openclaw gateway restart >> "$LOG_FILE" 2>&1
elif [ $EXIT_CODE -eq 1 ]; then
    echo "$(date '+%H:%M'): Warning state" >> "$LOG_FILE"
fi

# Output report (truncated for quiet mode)
head -10 "$REPORT_FILE"

exit 0  # Never propagate failures
