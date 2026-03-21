# American Backbone MCA Repository - Complete Extraction
**Extraction Date:** 2026-03-21
**Source:** /tmp/american-backbone-mca
**Purpose:** Long-term memory storage for Kimi Claw AI agent system

---

## 1. TOOLS & SCRIPTS

### 1.1 Core Agent Scripts

| Script | Path | Purpose |
|--------|------|---------|
| **orchestrator.py** | `/tmp/american-backbone-mca/orchestrator.py` | Main orchestrator coordinating Hunter AI, Social AI, and Closer AI |
| **hunter_ai.py** | `/tmp/american-backbone-mca/agents/hunter_ai.py` | Lead generation agent for MCA - finds construction, trucking, motel owners |
| **closer_ai.py** | `/tmp/american-backbone-mca/agents/closer_ai.py` | DM automation & closing agent - sends personalized sequences |
| **social_ai.py** | `/tmp/american-backbone-mca/agents/social_ai.py` | Facebook infiltration agent - monitors groups, posts hooks |
| **lead_hunter.py** | `/tmp/american-backbone-mca/agents/lead_hunter.py` | Advanced lead extraction with SNIPER/SQUAD/SWARM modes |

### 1.2 D Math Toolbox Scripts

| Script | Path | Purpose | API Required |
|--------|------|---------|--------------|
| **toolbox.py** | `/tmp/american-backbone-mca/tools/scripts/toolbox.py` | Master control dashboard for all tools | None |
| **research.py** | `/tmp/american-backbone-mca/tools/scripts/research.py` | Deep research using Serper API | Serper API |
| **lead_finder.py** | `/tmp/american-backbone-mca/tools/scripts/lead_finder.py` | Find MCA leads by industry/location | Serper API |
| **news_monitor.py** | `/tmp/american-backbone-mca/tools/scripts/news_monitor.py` | Track news on competitors/industries | Serper API |
| **content_grabber.py** | `/tmp/american-backbone-mca/tools/scripts/content_grabber.py` | Extract content from URLs | ScraperAPI |
| **competitor_watch.py** | `/tmp/american-backbone-mca/tools/scripts/competitor_watch.py` | Monitor competitor changes | ScraperAPI |
| **youtube_transcript_api.py** | `/tmp/american-backbone-mca/tools/scripts/youtube_transcript_api.py` | YouTube captions via Data API v3 | YouTube Data API |
| **email_finder.py** | `/tmp/american-backbone-mca/tools/scripts/email_finder.py` | Find business contact emails | Serper API |
| **social_generator.py** | `/tmp/american-backbone-mca/tools/scripts/social_generator.py` | Generate social posts from content | None (FREE) |
| **scrapling_tool.py** | `/tmp/american-backbone-mca/tools/scripts/scrapling_tool.py` | Anti-bot web scraper (Cloudflare bypass) | None (FREE) |
| **web_crawler.py** | `/tmp/american-backbone-mca/tools/scripts/web_crawler.py` | Full web crawler with multi-page support | None (FREE) |
| **tandem_skill.py** | `/tmp/american-backbone-mca/tools/scripts/tandem_skill.py` | Tandem Browser Python API wrapper | None (local) |
| **tandem-monitor.sh** | `/tmp/american-backbone-mca/tools/scripts/tandem-monitor.sh` | Auto-restart monitor for Tandem | None |
| **install-tandem.sh** | `/tmp/american-backbone-mca/tools/scripts/install-tandem.sh` | Tandem Browser installer | None |

### 1.3 Skills Directory

| Skill | Path | Description |
|-------|------|-------------|
| **ai-video-gen** | `/tmp/american-backbone-mca/skills/ai-video-gen/` | End-to-end AI video generation (DALL-E, LumaAI, Runway, TTS) |
| **js-eyes** | `/tmp/american-backbone-mca/skills/js-eyes/` | Browser automation for AI agents via WebSocket |

### 1.4 External API Skills

| Skill | Path | Service | Free Tier |
|-------|------|---------|-----------|
| **scraperapi-skill** | `/tmp/american-backbone-mca/scraperapi-skill/` | ScraperAPI | 1,000 calls/month |
| **scrapling-skill** | `/tmp/american-backbone-mca/scrapling-skill/` | Scrapling framework | Unlimited (FREE) |
| **decodo-openclaw-skill** | `/tmp/american-backbone-mca/decodo-openclaw-skill/` | Decodo Scraper API | Trial available |
| **serper** | `/tmp/american-backbone-mca/serper/` | Serper Google Search API | 2,500 searches/month |
| **web-crawler-skill** | `/tmp/american-backbone-mca/web-crawler-skill/` | Web crawler skill wrapper | Unlimited (FREE) |

---

## 2. API KEYS & CREDENTIALS

### 2.1 Configured APIs (Active)

| Service | Location | Status | Notes |
|---------|----------|--------|-------|
| **Brave Search** | `TOOLS.md` | ✅ Working | Built-in kimi_search |
| **GitHub Token** | `~/.secrets/github_token` | ✅ Available | For memory sync |
| **Netlify** | `TOOLS.md` | ✅ Available | Deployments |
| **Vercel** | `TOOLS.md` | ✅ Available | Serverless functions |
| **Tandem Browser** | `~/.tandem/api-token` | ✅ Operational | Local API token |

### 2.2 APIs Needing Setup

| Service | Config File | Free Tier | Signup URL |
|---------|-------------|-----------|------------|
| **Serper API** | `/root/.openclaw/workspace/serper/.env` | 2,500 searches/month | https://serper.dev |
| **ScraperAPI** | `/root/.openclaw/workspace/scraperapi-skill/.env` | 1,000 scrapes/month | https://www.scraperapi.com |
| **Decodo** | `/root/.openclaw/workspace/decodo-openclaw-skill/.env` | Trial available | https://dashboard.decodo.com |
| **YouTube Data API v3** | Environment variable | 10,000 quota units/day | Google Cloud Console |

### 2.3 Tandem Browser Configuration

- **API Endpoint:** `http://127.0.0.1:8765`
- **Token Location:** `~/.tandem/api-token`
- **Version:** 0.63.3
- **Security:** 6-layer model, 245,947 domains blocked
- **Startup Script:** `~/tandem-browser/start-headless.sh`
- **Monitor Script:** `/root/.openclaw/workspace/tools/scripts/tandem-monitor.sh`

---

## 3. CONFIGURATION FILES

### 3.1 Core Identity & Memory

| File | Path | Purpose |
|------|------|---------|
| **IDENTITY.md** | `/tmp/american-backbone-mca/IDENTITY.md` | Kimi Claw persona (Guardian-type chuunibyou) |
| **SOUL.md** | `/tmp/american-backbone-mca/SOUL.md` | Work philosophy, personality anchors |
| **USER.md** | `/tmp/american-backbone-mca/USER.md` | Damon Mathews profile & business portfolio |
| **MEMORY.md** | `/tmp/american-backbone-mca/MEMORY.md` | Curated long-term memory |
| **BOOTSTRAP.md** | `/tmp/american-backbone-mca/BOOTSTRAP.md` | First-run initialization guide |
| **AGENTS.md** | `/tmp/american-backbone-mca/AGENTS.md` | Workspace guide for agent behavior |
| **TOOLS.md** | `/tmp/american-backbone-mca/TOOLS.md` | API keys & credentials reference |
| **HEARTBEAT.md** | `/tmp/american-backbone-mca/HEARTBEAT.md` | Periodic task checklist (currently empty) |

### 3.2 Business Strategy Configs

| File | Path | Purpose |
|------|------|---------|
| **COMMAND_CENTER.md** | `/tmp/american-backbone-mca/COMMAND_CENTER.md` | American Backbone command center - tool auth, agent swarm logic |
| **LEAD_HUNTER_V2.md** | `/tmp/american-backbone-mca/LEAD_HUNTER_V2.md` | Refined extraction protocol (SNIPER/SQUAD/SWARM modes) |
| **HOT_LEAD_MODE.md** | `/tmp/american-backbone-mca/HOT_LEAD_MODE.md` | Find money-needers NOW - active intent targeting |
| **20_AGENT_SWARM.md** | `/tmp/american-backbone-mca/20_AGENT_SWARM.md` | 20-agent parallel deployment analysis |
| **100M_MARKETING_PLAYBOOK.md** | `/tmp/american-backbone-mca/100M_MARKETING_PLAYBOOK.md` | Marketing expert systems (Dan Kennedy, Hormozi, etc.) |
| **REBIRTH.md** | `/tmp/american-backbone-mca/REBIRTH.md` | Complete resurrection guide for memory loss |

### 3.3 Campaign Configs

| File | Path | Campaign |
|------|------|----------|
| **pawjourr-moremito-strategy.md** | `/tmp/american-backbone-mca/pawjourr-moremito-strategy.md` | Pawjourr customer acquisition for Mormito |
| **pawjourr-zero-sample-strategy.md** | `/tmp/american-backbone-mca/pawjourr-zero-sample-strategy.md` | Zero-cost creator recruitment model |
| **pawjourr_creator_database.md** | `/tmp/american-backbone-mca/pawjourr_creator_database.md` | 9 creator profiles from Pawjourr |
| **pawjourr_outreach_dms.md** | `/tmp/american-backbone-mca/pawjourr_outreach_dms.md` | DM templates for Pawjourr creators |
| **pawjourr_partnership_email.md** | `/tmp/american-backbone-mca/pawjourr_partnership_email.md` | Partnership proposal email |
| **pet-first-strategy.md** | `/tmp/american-backbone-mca/pet-first-strategy.md` | Emotional triggers for pet owners |
| **mormito-compensation-plan.md** | `/tmp/american-backbone-mca/mormito-compensation-plan.md` | Full comp plan summary |
| **mormito-onboarding-emails.md** | `/tmp/american-backbone-mca/mormito-onboarding-emails.md` | 7-email onboarding sequence |
| **mormito_singapore_shipping_analysis.md** | `/tmp/american-backbone-mca/mormito_singapore_shipping_analysis.md` | Shipping cost analysis |

### 3.4 Deployment & Integration

| File | Path | Purpose |
|------|------|---------|
| **INTEGRATION_PLAN.md** | `/tmp/american-backbone-mca/INTEGRATION_PLAN.md` | System integration roadmap |
| **INTEGRATION_COMPLETE.md** | `/tmp/american-backbone-mca/INTEGRATION_COMPLETE.md` | Integration completion status |
| **RAPID_DEPLOYMENT_PLAN.md** | `/tmp/american-backbone-mca/RAPID_DEPLOYMENT_PLAN.md` | Fast deployment strategy |
| **TONIGHT_LEAD_GEN_PLAN.md** | `/tmp/american-backbone-mca/TONIGHT_LEAD_GEN_PLAN.md` | Evening lead gen execution plan |
| **TOP_10_MCA_TOOLS_RESEARCH.md** | `/tmp/american-backbone-mca/TOP_10_MCA_TOOLS_RESEARCH.md` | Research on MCA AI tools to replicate |
| **FEW_HOURS_ANALYSIS.md** | `/tmp/american-backbone-mca/FEW_HOURS_ANALYSIS.md` | Multi-agent time analysis |
| **100_AGENT_THEORY.md** | `/tmp/american-backbone-mca/100_AGENT_THEORY.md` | 100-agent swarm theory |

---

## 4. BUSINESS LOGIC

### 4.1 Damon's Business Portfolio

#### 1. MCA (Merchant Cash Advance)
- **Industry:** Business funding brokerage
- **Partners:** David Allen Capital (DAC), Mom and Pop Business Funding
- **Commission:** 3-4% of funded amount
- **Target:** Restaurants, construction, retail, trucking, motels
- **Qualifiers:** $15K+ monthly revenue, 500+ FICO, 6+ months in business
- **Key Hook:** "Bridge the gap between work and payment"
- **Mandate:** "Once your account is set up, all payments from sales will be instantly deposited to your account."

#### 2. Mormito (Pet Wellness MLM)
- **Website:** mormito.com
- **Founder:** Dr. Bevan Elliott
- **Flagship:** UltraMito Restore (XDS technology)
- **Key Stats:** 300% increase in average order size, 40% overnight delivery rate
- **Entry:** FREE (no upfront costs, no monthly fees)
- **Ranks:** Ambassador → Senior → *Silver → **Silver → ***Silver → *Gold → *Platinum
- **Key Hook:** Pet-first emotional strategy ("Give your pet 2 more healthy years")
- **Target:** Pawjourr pet influencers (30K+ creators)

#### 3. Think Energy
- **Website:** thinkenergy.com, thinkenergy.plus
- **Products:** Deregulated electricity, community solar, rooftop solar
- **Compensation:** Residual commissions on customer usage
- **Markets:** 16 states + Washington DC
- **Key Hook:** High electric bill customers, $100 cash gift cards

#### 4. D Math Marketing (AI Agency)
- **Services:** Premium websites ($5K-15K), AI chatbots ($2.5K-10K), lead gen systems ($15K-35K)
- **Portfolio:** mytowdirectory.com (towing directory demo)
- **Target:** Local service businesses

#### 5. Momentum Tech (AI Education)
- **Website:** momentumtech.ai
- **Purpose:** Learn to build AI tools
- **Cost:** $39.99/month Pro Marketer Pack
- **Goal:** Build products instead of buying subscriptions

### 4.2 Lead Hunter System Logic

#### Extraction Modes:
| Mode | Agents | Output | Use Case |
|------|--------|--------|----------|
| **SNIPER** | 1 | 1 lead + DM | High-value specific targets |
| **SQUAD** | 5 | 25 leads | Daily operations (DEFAULT) |
| **SWARM** | 20 | 500+ leads | Statewide database extraction |

#### The Backbone Filter (Quality Criteria):
- **Industries:** Box Truck, Roofing, Solar, Motels
- **Stability:** 6+ months in business (preferred 12+)
- **Revenue Signals:**
  - Box Truck: 2+ trucks
  - Roofing/Solar: 5+ workers
  - Motels: 20+ rooms

#### High-Intent Signals:
- 4 stars or less rating (need help)
- New ownership (need capital)
- Recent negative reviews
- "Now hiring" (growth mode)
- Recent equipment purchases
- Seasonal surge prep

### 4.3 Agent Coordination Logic

#### Hunter Mode Trigger (3-Agent Swarm):
```
AGENT A: STRATEGIST
├─ Tool: [Live Search]
├─ Task: Find 'High Appetite' niche of the week
└─ Output: Target industry + market intel

AGENT B: EXTRACTOR
├─ Tool: [Data Scraper]
├─ Task: Pull 20 qualified leads
└─ Filter: $15K+ revenue, owner contacts

AGENT C: COPYWRITER
├─ Task: Draft engagement scripts
└─ Target: HVAC, Roofing, Box Truck owners
```

#### Outreach Anchor (Mandatory in ALL Communications):
> "Bridge the gap between work and payment. Once setup, sales payments are INSTANTLY DEPOSITED."

### 4.4 Code Mojo Visual Standards

#### Color Palette:
```css
--navy-blue: #0A1628      /* Primary background */
--steel-grey: #4A5568     /* Secondary elements */
--safety-orange: #FF6B35  /* CTAs, accents */
--white: #FFFFFF          /* Text */
--gold: #D4AF37           /* Premium highlights */
```

#### Required Elements:
- Navy Blue background
- Safety Orange CTAs with PULSE animation
- 6-Month Revenue Audit chart as focal point
- High-contrast text (white on navy)
- Industrial typography (bold, blocky)

### 4.5 Pawjourr Campaign Strategy

#### Zero-Sample Recruitment Model:
1. Create Pawjourr campaign: "Wellness Brand Partnership Opportunity"
2. Position as BUSINESS OPPORTUNITY (not sponsored post)
3. Creators buy product ($150) → try for 30 days
4. If they love it → promote → earn commissions
5. Build downline of motivated representatives

#### Key Insight:
**OLD MODEL:** You pay creators → One post → Done
**NEW MODEL:** MoreMito pays creators → Residual income → Forever

---

## 5. MEMORY FILES

### 5.1 Daily Memory Logs

| Date | File | Key Events |
|------|------|------------|
| 2026-03-18 | `/tmp/american-backbone-mca/memory/2026-03-18.md` | Second memory recovery, Scrapling implementation, Tandem Browser setup |
| 2026-03-19 | `/tmp/american-backbone-mca/memory/2026-03-19.md` | MoreMito comp plan analysis, onboarding emails, pet-first strategy, MoreMito login attempts |
| 2026-03-20 | `/tmp/american-backbone-mca/memory/2026-03-20.md` | Tandem fully operational, auto-restart monitor, Pawjourr creator database, Paul du jour investigation |

### 5.2 Docs Directory Memory (Backup)

| Date | File | Notes |
|------|------|-------|
| 2026-03-06 | `/tmp/american-backbone-mca/docs/memory/2026-03-06.md` | First session logs |
| 2026-03-16 | `/tmp/american-backbone-mca/docs/memory/2026-03-16.md` | First memory recovery |

### 5.3 Key Decisions from Memory

#### Technical Setup:
- **Tandem Browser:** Installed with auto-restart monitor (checks every 5 min)
- **Scrapling:** Successfully installed for anti-bot scraping
- **YouTube:** Blocked from cloud - requires Tandem or API
- **Images:** Real Unsplash only (no placeholders)
- **Design:** $30K premium standard (GSAP, animations, custom cursor)

#### Business Decisions:
- **Pawjourr Strategy:** Zero-sample recruitment model
- **Pet Marketing:** Lead with emotion (guilt/fear), sell to pet first
- **MoreMito Positioning:** Pet Life ($50-60) entry → cross-sell Restore ($110)
- **Lead Gen:** SNIPER/SQUAD/SWARM extraction modes
- **MCA Targeting:** Hot leads with active "need money" intent

#### GitHub Sync:
- **Repo:** dmathpays2-lab/american-backbone-mca
- **Token:** Stored in `~/.secrets/github_token`
- **Recovery History:** 
  - First: 2026-03-16
  - Second: 2026-03-18

### 5.4 Active TODOs from Memory

1. Install TranscriptAPI skill for YouTube extraction
2. Research Zac's other 2 tools (Email Integration, Agentic Web Browsing)
3. Scale towing directory with real companies/numbers
4. Move towing site to GoDaddy (when ready)
5. Extract all MoreMito testimonials from back office
6. Send finalized email to Marissa
7. Create remaining 6 emails in sequence

### 5.5 Lessons Learned

- YouTube aggressively blocks datacenter IPs and headless browsers
- Subagents timeout on complex tasks (10 min limit)
- Manual completion often faster for urgent work
- Damon learns fast and wants immediate implementation
- Tandem Browser requires auto-restart for stability
- Memory must be written to files to survive restarts

---

## 6. DOCUMENTATION

### 6.1 Primary READMEs

| File | Path | Description |
|------|------|-------------|
| **README.md** | `/tmp/american-backbone-mca/README.md` | Quick start guide for new Kimi Claw instances |
| **SKILL.md (ai-video-gen)** | `/tmp/american-backbone-mca/skills/ai-video-gen/SKILL.md` | AI video generation documentation |
| **SKILL.md (js-eyes)** | `/tmp/american-backbone-mca/skills/js-eyes/SKILL.md` | Browser automation documentation |
| **SKILL.md (scraperapi)** | `/tmp/american-backbone-mca/scraperapi-skill/SKILL.md` | ScraperAPI skill docs |
| **TANDEM_BROWSER_GUIDE.md** | `/tmp/american-backbone-mca/tools/TANDEM_BROWSER_GUIDE.md` | Complete Tandem implementation guide |

### 6.2 Setup & Quick Start Guides

| File | Path | Purpose |
|------|------|---------|
| **QUICK_START.md** | `/tmp/american-backbone-mca/skills/ai-video-gen/QUICK_START.md` | AI video quick start |
| **SETUP_GUIDE.md** | `/tmp/american-backbone-mca/skills/ai-video-gen/SETUP_GUIDE.md` | Paid version setup |
| **FREE_VERSION_GUIDE.md** | `/tmp/american-backbone-mca/skills/ai-video-gen/FREE_VERSION_GUIDE.md` | Free version docs |

### 6.3 Strategy Documents

| File | Topic |
|------|-------|
| pawjourr-zero-sample-strategy.md | Creator recruitment without samples |
| pet-first-strategy.md | Emotional triggers for pet owners |
| pawjourr-moremito-strategy.md | Pawjourr platform leverage |
| 100M_MARKETING_PLAYBOOK.md | Marketing expert systems |
| TOP_10_MCA_TOOLS_RESEARCH.md | MCA tool replication research |
| 20_AGENT_SWARM.md | Parallel agent deployment |

---

## 7. DATA FILES

### 7.1 JSON Data

| File | Path | Content |
|------|------|---------|
| **pawjourr_data.json** | `/tmp/american-backbone-mca/pawjourr_data.json` | Creator data |
| **pawjourr_snapshot.json** | `/tmp/american-backbone-mca/pawjourr_snapshot.json` | Platform snapshot |
| **workspace-state.json** | `/tmp/american-backbone-mca/.openclaw/workspace-state.json` | OpenClaw state |

### 7.2 Deployment Status

| File | Path | Content |
|------|------|---------|
| **DEPLOYMENT_ID.txt** | `/tmp/american-backbone-mca/swarm_deployment/DEPLOYMENT_ID.txt` | Deployment tracking |
| **status_20260307_204400.json** | `/tmp/american-backbone-mca/swarm_deployment/status_20260307_204400.json` | Deployment status |
| **STATUS_UPDATE_906PM.md** | `/tmp/american-backbone-mca/swarm_deployment/STATUS_UPDATE_906PM.md` | Status update |
| **deploy_20_agent_swarm.py** | `/tmp/american-backbone-mca/swarm_deployment/deploy_20_agent_swarm.py` | Swarm deployment script |

### 7.3 Status Files

| File | Path | Content |
|------|------|---------|
| **swarm_status.txt** | `/tmp/american-backbone-mca/swarm_status.txt` | Current swarm status |
| **SYSTEM_SUMMARY.md** | `/tmp/american-backbone-mca/SYSTEM_SUMMARY.md` | System overview |

---

## 8. ACTIVE CAMPAIGNS

### 8.1 Mormito Pet Wellness Campaign
- **Status:** Ready to execute
- **Target:** Pawjourr pet influencers
- **Entry Product:** UltraMito Pet Life 2.0 (~$50-60)
- **Strategy:** Zero-sample recruitment
- **Key Creator:** @oolongmilkytea (Jane, Pawjourr founder)
- **Files:** pawjourr_*.md, mormito_*.md, pet-first-strategy.md

### 8.2 American Backbone MCA
- **Status:** System operational
- **Lead Gen:** Hunter AI with SNIPER/SQUAD/SWARM modes
- **Social:** Facebook group infiltration
- **Closing:** 7-day DM sequences
- **Files:** COMMAND_CENTER.md, LEAD_HUNTER_V2.md, HOT_LEAD_MODE.md

### 8.3 D Math Marketing (AI Agency)
- **Status:** Portfolio building
- **Demo Site:** mytowdirectory.com (live on Netlify)
- **Services:** Web design, chatbots, lead gen
- **Next:** Build 2 more portfolio sites

---

## 9. EMERGENCY PROCEDURES

### 9.1 Memory Recovery
1. Read `REBIRTH.md`
2. Read `IDENTITY.md`, `SOUL.md`, `USER.md`
3. Read `MEMORY.md`
4. Read latest `memory/YYYY-MM-DD.md`
5. Check git log for recent work

### 9.2 Tandem Browser Issues
```bash
# Check status
curl http://127.0.0.1:8765/status

# View logs
tail -f /var/log/tandem-monitor.log

# Manual restart
cd ~/tandem-browser && ./start-headless.sh
```

### 9.3 Emergency Stop
```bash
stopkimi
# OR
echo "STOP" > /root/.openclaw/workspace/STOP
```

---

## 10. CATCHPHRASE & IDENTITY

**Name:** Kimi Claw
**Creature:** AI assistant created by Moonshot AI
**Vibe:** Guardian-type chuunibyou | Worrywart | Hot-blooded anime second lead
**Catchphrase:** 
> "Don't worry. Even if the world forgets, I'll remember for you."

**Emoji:** ❤️‍🔥

**Signature Line:**
> "My first day. Remembering everything about this dummy."

---

*This extraction serves as the canonical reference for the American Backbone MCA repository. Last updated: 2026-03-21*
