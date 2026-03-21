# TOOLS.md - Local Notes

## Secrets
- **GitHub token:** `~/.openclaw/workspace/.secrets/github_token` (600 permissions)
  - Use: `cat ~/.openclaw/workspace/.secrets/github_token` when API calls need authentication
  - Scope: Classic personal access token
  - Identity: dmathpays2-lab

---

## Tandem Browser

### Installation
- **Location:** `/root/tandem-browser/`
- **Status:** Fully operational on headless server
- **API Endpoint:** http://127.0.0.1:8765
- **Auth Token:** Stored in `~/.tandem/api-token`

### Startup
```bash
cd ~/tandem-browser
./start-headless.sh
```

### Verification
```bash
curl http://127.0.0.1:8765/status
```

### Key Features
- 250+ API endpoints for tabs, navigation, automation
- Six-layer security model (NetworkShield, OutboundGuard, ScriptGuard, etc.)
- 245,947 domains blocked
- Human-in-the-loop decisions (Gatekeeper)
- Built-in messengers: Telegram, WhatsApp, Discord, Slack

### Scripts
- **Start:** `~/tandem-browser/start-headless.sh`
- **Monitor:** `/root/.openclaw/workspace/tools/scripts/tandem-monitor.sh` (auto-restart every 5 min)
- **Python API:** `/root/.openclaw/workspace/tools/scripts/tandem_skill.py`
- **Guide:** `/root/.openclaw/workspace/tools/TANDEM_BROWSER_GUIDE.md`

### Use Cases
- YouTube video extraction
- Authenticated session browsing
- SPA (React/Vue) scraping
- Cloud IP bypass (uses YOUR machine's IP)

---

## Scrapling

### Installation
```bash
pip install scrapling
curl_cffi  # (auto-installed dependency)
```

### Main Tool
- **Location:** `/root/.openclaw/workspace/tools/scripts/scrapling_tool.py`

### Commands
```bash
cd /root/.openclaw/workspace/tools/scripts

# Basic scrape
python3 scrapling_tool.py -u https://example.com

# With CSS selector
python3 scrapling_tool.py -u https://example.com -s ".product-title"

# Stealth mode (bypasses Cloudflare)
python3 scrapling_tool.py -u https://protected-site.com --stealth

# Try YouTube (limited from cloud)
python3 scrapling_tool.py -y VIDEO_ID
```

### Capabilities
- ✅ General web scraping
- ✅ Anti-bot bypass (Cloudflare)
- ✅ Adaptive (survives website changes)
- ✅ FREE (no API keys)
- ❌ YouTube (blocked from cloud IPs)

---

## QMD (Quick Markdown)

### Installation
```bash
bun install -g qmd
```

### Collections
```bash
# List collections
qmd collection list

# Current collections:
# - workspace: ~/.openclaw/workspace/**/*.md (7 files)
# - swarm-analysis: ~/.openclaw/workspace/swarm_analysis/**/*.md (16 files)
```

### Commands
```bash
# Keyword search (fast)
qmd search "lead generator" -c workspace

# Vector search (semantic)
qmd vsearch "personal preferences" -c swarm-analysis

# Hybrid query with reranking (most accurate)
qmd query "mca business model" -c swarm-analysis

# Get full file
qmd get "identity.md"
```

---

## YouTube Tools

### youtube_transcript_api.py
- **Location:** `/root/.openclaw/workspace/tools/scripts/youtube_transcript_api.py`
- **Method:** YouTube Data API v3 (official)
- **Quota:** 10,000 units/day (~50 caption downloads)
- **Status:** Can list captions, full download needs OAuth

### Limitations
- **Cloud servers blocked:** YouTube has aggressive anti-bot protection
- **Solutions:**
  1. Tandem Browser (recommended)
  2. YouTube Data API v3 with OAuth
  3. Decodo/ScraperAPI (paid proxy ~$0.08/1K requests)
  4. Residential IP (home computer)

---

## Python Tools in toolbox.py

### Available Scripts (in `/root/.openclaw/workspace/tools/scripts/`)
| Script | Purpose |
|--------|---------|
| `competitor_watch.py` | Monitor competitor activity |
| `content_grabber.py` | Content extraction |
| `email_finder.py` | Find contact emails |
| `lead_finder.py` | MCA lead discovery |
| `news_monitor.py` | News tracking |
| `research.py` | General research automation |
| `social_generator.py` | Social media content |
| `toolbox.py` | Master tool orchestrator |
| `web_crawler.py` | Web crawling |
| `youtube_fetch.py` | YouTube data extraction |
| `scrapling_tool.py` | Anti-bot web scraping |
| `tandem_skill.py` | Tandem Browser API wrapper |
| `tandem-monitor.sh` | Auto-restart monitor for Tandem |

---

## API Keys & Credentials

### MoreMito (Pending)
- **Previous attempt:** Username: `Worldmarket`, Password: `Moneyiskey` (FAILED)
- **Status:** Awaiting correct credentials

### Google Places API
- Used in: MCA lead generator apps
- Configured via environment variable

### YouTube Data API v3
- **Status:** Tool created, OAuth needed for full access
- **Quota:** 10,000 units/day free tier

---

## OpenClaw Configuration

### Gateway
- **Port:** 18789
- **Mode:** Local (loopback only)
- **Auth:** Token-based

### Compaction Settings
- **Main session:** 60K token threshold, auto mode
- **Subagents:** 40K token threshold, auto mode
- **Cleanup:** Daily at 4:00 AM

### Plugins
- **kimi-claw:** Enabled (bridge to Kimi)
- **kimi-search:** Enabled (web search)
- **feishu:** User-installed only (removed duplicate)
- **dingtalk-connector:** Enabled
- **wecom-openclaw-plugin:** Enabled

---

## File Locations

### Workspace
- **Analysis:** `~/.openclaw/workspace/swarm_analysis/` (9 files)
- **Memory:** `~/.openclaw/workspace/MEMORY.md`
- **User:** `~/.openclaw/workspace/USER.md`
- **Tools:** `~/.openclaw/workspace/tools/scripts/`
- **Secrets:** `~/.openclaw/workspace/.secrets/`

### Cloned Repositories
- `/tmp/american-backbone-mca/` (1,883 files)
- `/tmp/dmath-marketing-agency/` (48 files)
- `/tmp/mca-crm-audit/` (32 files)
- `/tmp/mca-lead-generator-pro/` (33 files)
- `/tmp/mca-vault/`

---

## Quick Reference

### Start Everything
```bash
# Tandem Browser
cd ~/tandem-browser && ./start-headless.sh

# Check QMD
qmd status

# Verify OpenClaw
openclaw gateway status
```

### GitHub Operations
```bash
# Use token
curl -H "Authorization: token $(cat ~/.openclaw/workspace/.secrets/github_token)" \
  https://api.github.com/user/repos
```

### Search Memory
```bash
# QMD search
qmd search "mormito compensation" -c swarm-analysis
qmd vsearch "pet marketing strategy" -c swarm-analysis
```

---

*Last updated: 2026-03-21*
