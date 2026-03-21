# American Backbone MCA - Repository Analysis

**Repository:** dmathpays2-lab/american-backbone-mca  
**Owner:** Damon Mathews  
**Purpose:** AI Agent Swarm for MCA (Merchant Cash Advance) Lead Generation  
**Analysis Date:** 2026-03-21

---

## 1. Top-Level Directory Structure

| Directory | Purpose |
|-----------|---------|
| `agents/` | Core AI agent implementations (Lead Hunter, Closer AI, Social AI) |
| `swarm_deployment/` | 20-agent swarm deployment scripts and status tracking |
| `tools/` | Research, scraping, and utility scripts |
| `skills/` | OpenClaw skill modules (AI video gen, JS eyes) |
| `docs/` | Documentation templates (AGENTS.md, IDENTITY.md, MEMORY.md, etc.) |
| `memory/` | Daily log files (2026-03-18.md, 2026-03-19.md, 2026-03-20.md) |
| `.openclaw/` | OpenClaw workspace state |
| `scraperapi-skill/` | ScraperAPI integration for web scraping |
| `scrapling-skill/` | Free anti-bot web scraping (Scrapling framework) |
| `serper/` | Serper API integration for Google search |
| `decodo-openclaw-skill/` | Decodo proxy service (empty - not yet configured) |
| `web-crawler-skill/` | Web crawling skill documentation |

---

## 2. Main Entry Points

| Entry Point | Purpose | Type |
|-------------|---------|------|
| `orchestrator.py` | **PRIMARY** - CEO Agent that coordinates Hunter AI, Social AI, and Closer AI | Main |
| `agents/lead_hunter.py` | Advanced Lead Extraction System with SNIPER/SQUAD/SWARM modes | Agent |
| `agents/hunter_ai.py` | Lead generation agent for construction/trucking/motel owners | Agent |
| `agents/closer_ai.py` | DM automation and closing sequence agent | Agent |
| `agents/social_ai.py` | Facebook infiltration and content generation agent | Agent |
| `swarm_deployment/deploy_20_agent_swarm.py` | 20-agent parallel deployment for rapid tool building | Deployment |
| `tools/scripts/toolbox.py` | Unified CLI for all research tools | Utility |
| `extract_pdf.py` | PDF content extraction utility | Utility |

### Orchestrator Flow
```
User Request → orchestrator.py
    ├── Hunter AI (lead finding)
    ├── Social AI (Facebook content)
    └── Closer AI (DM automation)
```

---

## 3. Key Modules/Components

### 3.1 Agent System (Core)

#### `LeadHunter` (`agents/lead_hunter.py`)
- **Modes:** SNIPER (1 target), SQUAD (25 leads), SWARM (statewide)
- **Target Industries:** Box Truck, Roofing, Solar, Motels
- **Filters:** $15K+ revenue, 500+ FICO, 6+ months in business
- **High-Intent Signals:** 4-star or less ratings, new ownership

#### `CloserAI` (`agents/closer_ai.py`)
- **Purpose:** DM automation and closing sequences
- **Features:** 7-day closing sequence, objection handling, response tracking
- **Scripts:** Initial DM, 24h follow-up, 48h follow-up, value nurture

#### `SocialAI` (`agents/social_ai.py`)
- **Purpose:** Facebook infiltration and lead generation
- **Content Types:** UNSTOPPABLE posts, Opinion hooks, Search & Rescue comments
- **Monitoring:** Auto-detects trigger keywords in Facebook groups

### 3.2 Research Tools (`tools/scripts/`)

| Tool | Purpose | API Required |
|------|---------|--------------|
| `research.py` | Deep topic research | Serper |
| `lead_finder.py` | MCA lead discovery | Serper |
| `news_monitor.py` | Topic tracking | None (scheduled) |
| `competitor_watch.py` | Competitor monitoring | ScraperAPI |
| `content_grabber.py` | URL content extraction | None |
| `email_finder.py` | Business contact discovery | Serper |
| `social_generator.py` | Social media post generation | **None** |
| `youtube_transcript.py` | YouTube transcript extraction | Decodo/Free |
| `web_crawler.py` | Anti-bot web crawling | **None** (Scrapling) |
| `scrapling_tool.py` | Scrapling integration | **None** |
| `tandem_skill.py` | Tandem Browser automation | Local service |

### 3.3 Skills (`skills/`)

| Skill | Purpose | Dependencies |
|-------|---------|--------------|
| `ai-video-gen/` | AI video generation | openai, replicate, pillow |
| `js-eyes/` | JavaScript analysis tool | Node.js packages |

---

## 4. Tech Stack & Dependencies

### Core Technologies
- **Language:** Python 3.x
- **Framework:** OpenClaw Agent System
- **Browser Automation:** Tandem Browser (Playwright-based)

### Python Dependencies

#### Required (from various skill files):
```
openai>=1.0.0
replicate>=0.20.0
requests>=2.31.0
pillow>=10.0.0
python-dotenv>=1.0.0
scrapling
curl_cffi
beautifulsoup4
lxml
PyPDF2
```

#### Web Scraping Stack:
| Tool | Type | Free Tier |
|------|------|-----------|
| **Scrapling** | Open-source scraper | Unlimited |
| **Serper API** | Google Search API | 2,500/month |
| **ScraperAPI** | Proxy scraper | 1,000/month |
| **Decodo** | Residential proxies | Paid (~$0.08/1K) |

### External Services
- **Tandem Browser:** Local headless browser service (http://127.0.0.1:8765)
- **GitHub:** Repository storage and backup
- **YouTube Data API v3:** For transcript extraction (50 captions/day free)

### API Keys (Required)
1. `SERPER_API_KEY` - `/root/.openclaw/workspace/serper/.env`
2. `SCRAPERAPI_KEY` - `/root/.openclaw/workspace/scraperapi-skill/.env`
3. GitHub token - `~/.openclaw/workspace/.secrets/github_token`

---

## 5. Business Context

**Damon's Portfolio:**
1. **MCA (American Backbone)** - Business funding brokerage
2. **Mormito** - Pet wellness MLM
3. **Think Energy** - Electricity/solar sales
4. **D Math Marketing** - AI agency services

**AI Agent Identity:**
- **Name:** Kimi Claw
- **Persona:** Guardian-type chuunibyou AI
- **Catchphrase:** "Don't worry. Even if the world forgets, I'll remember for you."

---

## 6. Key Files Summary

| File | Purpose |
|------|---------|
| `README.md` | Quick start guide for AI rebirth |
| `REBIRTH.md` | Complete resurrection documentation |
| `IDENTITY.md` | AI agent identity and personality |
| `SOUL.md` | Personality and interaction style |
| `USER.md` | Damon's business portfolio and goals |
| `AGENTS.md` | Agent system documentation |
| `MEMORY.md` | Long-term memory storage |
| `COMMAND_CENTER.md` | Command interface documentation |
| `HEARTBEAT.md` | Periodic check instructions |

---

## 7. Operational Notes

### Daily Workflow
1. Read `HEARTBEAT.md`
2. Review today's memory file
3. Check Tandem Browser status
4. Run orchestrator or individual agents
5. Update memory files
6. Commit changes to GitHub

### Key URLs
- Tandem Browser: `http://127.0.0.1:8765`
- GitHub Repo: `https://github.com/dmathpays2-lab/american-backbone-mca`

### Limitations
- YouTube blocks cloud IPs (use API instead)
- Some sites require stealth mode for Scrapling
- API rate limits apply (Serper: 2,500/mo, ScraperAPI: 1,000/mo)
