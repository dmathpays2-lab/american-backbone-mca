# TANDEM_BROWSER_GUIDE.md

## Tandem Browser - Operational

**Status:** ✅ Fully operational on headless Linux server  
**Version:** 0.65.5  
**API:** http://127.0.0.1:8765  
**Token:** ~/.tandem/api-token

---

## Quick Start

```bash
# Start Tandem
cd ~/tandem-browser
./start-headless.sh

# Check status
curl http://127.0.0.1:8765/status

# Verify with token
TOKEN=$(cat ~/.tandem/api-token)
curl http://127.0.0.1:8765/tabs/list \
  -H "Authorization: Bearer $TOKEN"
```

---

## Python API Usage

```python
from tools.scripts.tandem_skill import TandemBrowser

tandem = TandemBrowser()

# Open a tab
tab = tandem.open_tab("https://example.com")

# Get page snapshot
snapshot = tandem.get_snapshot()

# Extract YouTube info
info = tandem.extract_youtube_info("https://youtube.com/watch?v=VIDEO_ID")
```

---

## Key Features

- ✅ 250+ API endpoints
- ✅ 6-layer security model
- ✅ Auto-restart monitor (5-min checks)
- ✅ YouTube extraction capability
- ✅ Authenticated session browsing
- ✅ SPA (React/Vue) scraping

---

## Troubleshooting

**Tandem not responding:**
```bash
# Check if running
ps aux | grep electron

# Restart
kill $(cat ~/tandem-browser/.tandem.pid)
~/tandem-browser/start-headless.sh
```

**Monitor logs:**
```bash
tail -f /var/log/tandem-monitor.log
```

---

*Installed: 2026-03-21*
