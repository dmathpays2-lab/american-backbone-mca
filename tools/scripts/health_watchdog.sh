#!/bin/bash
# OpenClaw timeout watchdog - kills runs before they die of old age
# Run this every 2 minutes via cron

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPORT_FILE="/root/.openclaw/workspace/.health_report.txt"

# Run health check
python3 "$SCRIPT_DIR/health_monitor.py" > "$REPORT_FILE" 2>&1
EXIT_CODE=$?

# If critical (gateway down), try to restart
if [ $EXIT_CODE -eq 2 ]; then
    echo "$(date): Gateway down, attempting restart..." >> /root/.openclaw/logs/health_watchdog.log
    openclaw gateway restart
fi

# Always output the report for debugging
cat "$REPORT_FILE"

exit $EXIT_CODE
