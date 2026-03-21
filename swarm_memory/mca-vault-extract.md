# MCA Vault - Complete Repository Extraction
## American Backbone AI Agent Swarm System
**Extracted:** March 21, 2026  
**Source:** /tmp/american-backbone-mca, /tmp/mca-crm-audit, /tmp/mca-lead-generator-pro  
**User:** Damon Mathews (damon@bizfunds.net)

---

# 1. AI AGENT SWARM

## Overview
The American Backbone system uses a multi-agent AI swarm architecture to automate MCA (Merchant Cash Advance) lead generation, qualification, and closing. The system operates with 3 core agents coordinated by a CEO/Orchestrator agent.

## Core Agents

### 1.1 Lead Hunter V2 (`agents/lead_hunter.py`)
**Purpose:** Primary lead extraction and qualification

**Extraction Modes:**
- **SNIPER Mode:** 1 agent, precision strike on single high-value target
  - Use case: Target specific owner, referral follow-up
  - Output: 1 fully researched lead with drafted DM
  - Command: `"SNIPER: Mike Johnson at Johnson Trucking"`
  - Time: ~10 minutes

- **SQUAD Mode:** 5 agents, standard daily deployment (DEFAULT)
  - Use case: Daily operations, consistent pipeline
  - Output: 20-30 qualified leads
  - Command: `"SQUAD: Houston, Box Truck, 25"`
  - Time: ~1 hour
  - Agents:
    - Agent 1: [Live Search] - Find businesses
    - Agent 2: [Maps Scraper] - Extract details
    - Agent 3: [Email/Phone Extractor] - Get owner contacts
    - Agent 4: Review analyzer - Check ratings/ownership
    - Agent 5: Filter validator - Apply BACKBONE criteria

- **SWARM Mode:** 20 agents, statewide database extraction
  - Use case: Major campaigns, new state entry
  - Output: 500-1000+ leads
  - Command: `"SWARM: Texas, Box Truck|Roofing|Motels"`
  - Time: ~4 hours
  - ⚠️ Warning: High resource usage

**THE BACKBONE FILTER (Quality Control):**
```python
BACKBONE_CRITERIA = {
    "industries": ["Box Truck", "Roofing", "Solar", "Motels"],
    "stability": {
        "min_months_in_business": 6,
        "preferred": "12+ months"
    },
    "revenue_signals": {
        "box_truck": "Multiple trucks (2+)",
        "roofing_solar": "Large crews (5+ workers)",
        "motels": "20+ rooms"
    }
}
```

**HIGH-INTENT SIGNALS:**
- "4 stars or less" rating (need help)
- New ownership (need capital)
- Recent negative reviews
- Now hiring (growth mode)
- Recent equipment purchases

**MANDATORY OUTREACH ANCHOR:**
> "Bridge the gap between work and payment. Once setup, sales payments are INSTANTLY DEPOSITED."

---

### 1.2 Social AI (`agents/social_ai.py`)
**Purpose:** Facebook infiltration and content automation

**Functions:**
- Creates 4 posts/day per niche (trucking, construction, motels)
- Monitors 15+ Facebook groups
- Auto-responds to trigger posts
- Auto-DM responders

**Post Types:**
1. **UNSTOPPABLE Posts:** Red background, direct CTA
   - Template: "Waiting 30-60 days for payouts? 🚛💨 I have a way to bridge the gap. Comment 'TRUCK' for info!"
   - Trigger words: TRUCK, CASH, FLOW, NOW, BRIDGE

2. **OPINION HOOK Posts:** Bypasses AI spam filters
   - Template: "Are these brokers getting slower with the checks this month? 🚛💨 Or is it just me?"
   - Creates engagement, identifies prospects

3. **SEARCH & RESCUE Comments:** Respond to others' pain posts
   - Template: "I'm seeing that 30-day gap hitting a lot of fleets this month. I've got a strategy guide..."

4. **Value Posts:** Authority building
   - Quick tips about revenue-based funding
   - Success stories
   - Industry insights

**Target Groups by Niche:**
- Trucking: Owner Operator Trucking, Truckers USA, Hotshot Trucking, Box Truck Business
- Construction: Construction Business Owners, Roofing Contractors, HVAC Business Owners
- Motels: Hotel & Motel Owners, Independent Hotel Owners, Hospitality Business Owners

**Auto-DM Template:**
```
Hey! Thanks for reaching out about bridging that cash flow gap.

I help {niche} owners access working capital in 24-48 hours using a 
6-month revenue audit - no credit check games, no waiting 30-60 days.

Quick qualifiers:
• $15K+ monthly revenue (last 6 months)
• 500+ FICO
• 6+ months in business

Want to see your funding capacity? Just reply and I'll run the numbers.

- Damon | American Backbone
```

---

### 1.3 Closer AI (`agents/closer_ai.py`)
**Purpose:** DM automation and closing sequences

**7-Day Closing Sequence:**
| Day | Message Type | Goal |
|-----|--------------|------|
| 0 | Initial DM | Send strategy guide, introduce service |
| 1 | 24h Follow-up | Check if guide received, ask about urgency |
| 2 | 48h Follow-up | Social proof, soft CTA |
| 4 | Value Nurture | Provide value, stay top of mind |
| 7 | Final Touch | Last follow-up, leave door open |

**Initial DM Template:**
```
Hey {name}, I'm Damon with American Backbone. Here is that info on 
bridging the 30-60 day gap.

We use a 180-day revenue audit to get you funded while you wait on 
those slow broker payouts.

**OUR 2026 BENCHMARKS:**
• $15k+ Monthly Revenue (Last 6 Months)
• 500+ FICO Score
• 6 Months in Business

**Note:** Once your account is set up, all payments from sales will be 
instantly deposited to your account.

Here is the Strategy Guide: [LINK]

Want to see your funding capacity today?
```

**Objection Handlers:**
- "Too expensive" → Position as bridge capital, not expense
- "Bad credit" → Based on revenue, not personal credit
- "Not interested" → Ask about current strategies
- "Need to think" → Offer no-obligation capacity check
- "Too busy" → Fast 10-minute process

---

### 1.4 Hot Lead Hunter (`HOT_LEAD_MODE.md`)
**Purpose:** Real-time intent detection for immediate money pain

**Money Pain Signals:**
- 🔥🔥🔥 HIGHEST INTENT: "need money fast", "can't make payroll", "bills due", "desperate for cash"
- 🔥🔥 HIGH INTENT: "payout delay", "30 days late", "broker slow", "cash flow gap"
- 🔥 MEDIUM INTENT: "funding options", "business loan", "line of credit"

**6-Agent Hot Lead Deployment:**
1. **Agents 1-2:** 6sense-intent (Find active posts)
2. **Agent 3:** Seamless-rapid (Get phone numbers)
3. **Agent 4:** Apollo-hot (Find distressed businesses)
4. **Agent 5:** Clay-hot (Create urgency outreach)
5. **Agent 6:** Commander-hot (Quality control)

**Timeline (Friday 6:30 PM Iowa):**
- 6:30 PM: Deploy 6 agents
- 8:00 PM: 20+ hot leads identified
- 9:00 PM: Contact info extracted
- 10:00 PM: Personalized DMs drafted

---

# 2. ORCHESTRATOR / CEO AGENT

## AmericanBackboneOrchestrator (`orchestrator.py`)

**Role:** Central coordinator that manages all agents and routes user requests

**Architecture:**
```
┌─────────────────────────────────────────┐
│         KIMI ORCHESTRATOR (You)        │
└──────────────────┬──────────────────────┘
                   │
┌──────────────────┴──────────────────────┐
│         AGENT 20 (COMMANDER)           │
│    - Assigns tasks to agents 1-19      │
│    - Resolves conflicts                │
│    - Reports progress                  │
└──────────────────┬──────────────────────┘
                   │
    ┌──────────────┼──────────────┐
    │              │              │
┌───┴───┐    ┌───┴───┐    ┌───┴───┐
│INFRA  │    │BUILD  │    │QA     │
│(1-4)  │    │(5-16) │    │(17-19)│
└───────┘    └───────┘    └───────┘
```

**Daily Operations:**
1. Activates Lead Hunter AI (SNIPER/SQUAD/SWARM modes)
2. Activates Social AI (Facebook content creation)
3. Activates Closer AI (DM automation)
4. Generates morning briefing for Damon

**Daily Stats Tracked:**
- Leads generated
- Posts created
- DMs sent
- Responses received
- Calls booked

**User Request Routing:**
- "Find leads" → Hunter AI
- "Facebook post" → Social AI  
- "Send follow-up" → Closer AI

**Morning Briefing Includes:**
- Today's mission for each agent
- Hot lead opportunities
- Messaging strategy
- Targets (Leads, DMs, Responses, Calls, Deals)

---

# 3. API STRUCTURE (Vercel)

## Backend: MCA CRM Application (`/tmp/mca-crm-audit/`)

**Tech Stack:**
- Frontend: Vanilla HTML/CSS/JS (Single Page Application)
- Backend: Node.js/Express (implied from vercel.json)
- Data: localStorage (client-side persistence)
- Deployment: Vercel

**vercel.json Configuration:**
```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.js",
      "use": "@vercel/node"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "/index.html"
    }
  ]
}
```

**Data Model (localStorage):**
```javascript
const defaultData = {
    leads: [...],           // Business leads
    activities: [...],      // Contact history
    followUps: [...],       // Scheduled follow-ups
    funders: [...],         // Lender database
    commissions: [...],     // Monthly commission history
    user: {...}             // User profile & settings
}
```

**Lead Stages:**
1. new_lead
2. contacted
3. qualified
4. application_sent
5. submitted_to_funder
6. approved
7. funded
8. paid

**Funder Tiers:**
- Tier 1 (Beginner): $5K-75K, 8-9% commission, 24-48h turnaround
- Tier 2 (Intermediate): $25K-200K, 10-11% commission, 48-72h turnaround
- Tier 3 (Advanced): $50K-500K, 12% commission, 72h turnaround
- Tier 4 (Premium): $100K-2M, 15% commission, 96h turnaround

**Key Features:**
- Lead scoring (0-100 based on revenue, age, industry, contact quality)
- Pipeline visualization (Kanban board)
- Calendar with follow-ups
- Commission tracking with charts
- Funder management
- Activity logging

---

# 4. BACKEND (Node.js/Express + Stripe)

## Premium Landing Page (`/tmp/mca-lead-generator-pro/`)

**Files:**
- `index.html` - Main landing page
- `premium.html` - Premium version
- `app.js` - Backend logic
- `vercel.json` - Vercel deployment config

**Lead Qualification Criteria (from landing page):**
- ✅ $15K+ monthly revenue
- ✅ 500+ FICO score
- ✅ 6+ months in business

**Industry Targets:**
- Box Truck / Trucking
- Roofing
- Solar
- Motels

**Visual Design System (Code Mojo):**
```css
:root {
  --navy-blue: #0A1628;        /* Primary background */
  --steel-grey: #4A5568;       /* Secondary elements */
  --safety-orange: #FF6B35;    /* CTAs, accents */
  --white: #FFFFFF;            /* Text */
  --gold: #D4AF37;             /* Premium highlights */
}
```

**Required Visual Elements:**
- Navy Blue background (#0A1628)
- Steel Grey cards (#4A5568)
- Safety Orange CTAs with pulse animation
- 6-Month Revenue Audit chart (focal point)
- High-contrast text (white on navy)
- Industrial typography (bold, blocky)

**CTA Pulse Animation:**
```css
@keyframes pulse {
  0% { box-shadow: 0 0 0 0 rgba(255, 107, 53, 0.7); }
  70% { box-shadow: 0 0 0 15px rgba(255, 107, 53, 0); }
  100% { box-shadow: 0 0 0 0 rgba(255, 107, 53, 0); }
}
```

**INSTANT DEPOSIT MANDATE (All Communications):**
> "Once your account is set up, all payments from sales will be instantly deposited to your account."

---

# 5. BUSINESS LOGIC

## MCA Qualification Criteria

### Hard Requirements:
| Criteria | Minimum | Preferred |
|----------|---------|-----------|
| Monthly Revenue | $15,000 | $50,000+ |
| FICO Score | 500 | 650+ |
| Time in Business | 6 months | 12+ months |

### Target Industries (Backbone Filter):
1. **Box Truck / Trucking**
   - Signal: Multiple trucks (2+)
   - Pain: 30-60 day broker payout delays
   - Seasonal: Spring surge, spot market volatility

2. **Roofing**
   - Signal: Large crews (5+ workers)
   - Pain: Material costs upfront, client payment delays
   - Seasonal: Spring construction season

3. **Solar**
   - Signal: Large crews (5+ workers)
   - Pain: Long installation cycles, delayed commissions
   - Seasonal: Spring/summer installation rush

4. **Motels**
   - Signal: 20+ rooms
   - Pain: Seasonal fluctuations, occupancy gaps
   - Seasonal: Spring break season (FL/AZ)

### Rejection Criteria:
- ❌ Industry not in target list
- ❌ Less than 6 months in business
- ❌ Revenue signals insufficient
- ❌ No owner contact found

## Targeting Strategy

### High-Intent Signals:
- "4 stars or less" ratings (reputation/cash flow issues)
- "New ownership" (acquisition debt needs)
- "Under new management" (turnaround capital)
- Recent negative reviews mentioning "slow pay"
- "Now hiring" + growing fast (cash flow gap)

### Geographic Focus:
- Houston, TX
- Phoenix, AZ
- Atlanta, GA
- Miami, FL
- Dallas, TX

### Outreach Hooks by Industry:
**Box Truck:**
- Hook: "Bridge the gap between loads and payment"
- Pain: "waiting 30-60 days for broker payouts"
- Solution: "180-day revenue audit for immediate funding"

**Roofing:**
- Hook: "Bridge the gap between jobs and payment"
- Pain: "material costs upfront, client payments delayed"
- Solution: "revenue-based funding in 24-48 hours"

**Solar:**
- Hook: "Bridge the gap between installs and payment"
- Pain: "long installation cycles, delayed commissions"
- Solution: "6-month revenue audit for working capital"

**Motels:**
- Hook: "Bridge the gap between bookings and cash flow"
- Pain: "seasonal fluctuations, occupancy gaps"
- Solution: "revenue-based funding for improvements"

## Commission Structure

### Partner Platforms:
1. **David Allen Capital (DAC)**
   - Commission: 3-4% of funded amount
   - Next-day payouts
   - Bank Breezy™ platform (one application, 30+ lenders)
   - Team building with overrides

2. **Mom and Pop Business Funding**
   - Up to $1M per deal
   - 2.7M+ customers served, $23B+ funded since 2007
   - Founded by Bret Martin (#1 MCA producer 3 years)
   - Same-day to 1-2 day funding
   - Strong on renewals/repeat business

### Commission Calculator (Example):
- 25 leads/day × 22 days = **550 leads/month**
- High-intent flagged: ~30% = **165 hot leads**
- Calls booked: ~15% = **82 calls**
- Deals funded: ~10% = **55 deals**
- **Commission: $165K/month** (at $3K avg commission per deal)

---

# 6. COST MODEL

## AI Agent Swarm vs Human Team Comparison

### AI Agent Swarm Costs:

**Monthly API Costs:**
| Service | Cost/Month | Tools Using |
|---------|-----------|-------------|
| OpenAI | $200 | All 10 |
| Brave Search | $50 | Apollo, Clay, 6sense, Baselayer |
| Hunter.io | $50 | Seamless |
| Twilio | $30 | Enginy, Instantly |
| SMTP | $20 | Enginy, Instantly, Lavender |
| **TOTAL** | **$350/mo** | |

**Deployment Costs:**
- 6-Day Blitz (10 agents): ~$500 in APIs
- 20-Agent SWARM (2.5 hours): ~$330
- 100-Agent theoretical: ~$1,150

**Optimal Configuration:**
- **20 agents for 3 hours = $300**
- Success rate: 95%
- All 10 tools operational

### Human Team Equivalent:

| Role | Salary/Month | Annual Cost |
|------|--------------|-------------|
| Lead Generation Specialist | $4,000 | $48,000 |
| Sales Development Rep (2x) | $3,500 × 2 | $84,000 |
| Account Executive | $5,000 | $60,000 |
| Marketing Manager | $5,000 | $60,000 |
| CRM/Operations Manager | $4,000 | $48,000 |
| **TOTAL** | **$24,000/mo** | **$288,000/year** |

### Cost Comparison Summary:

| Metric | AI Swarm | Human Team | Savings |
|--------|----------|------------|---------|
| **Monthly Cost** | ~$450 (APIs + compute) | ~$12,000 (5 FTEs) | **96%** |
| **Setup Time** | 6 days | 3-6 months | **98%** |
| **Scale Speed** | Instant (add agents) | 4-8 weeks (hiring) | **95%** |
| **24/7 Operation** | Yes | No (business hours) | **-** |
| **Consistency** | 100% | Variable | **-** |
| **Lead Volume** | 550/month | 200/month | **175%** |

### ROI Calculation:

**AI Swarm:**
- Cost: $450/month
- Output: 550 leads/month → 55 deals/month
- Revenue: $165K commission/month
- **ROI: 36,567%**

**Human Team:**
- Cost: $12,000/month
- Output: 200 leads/month → 20 deals/month
- Revenue: $60K commission/month
- **ROI: 400%**

**Net Advantage:**
- **$105K MORE commission per month**
- **$105K LESS cost per month**
- **$210K net positive swing**

---

# 7. THE 10 MCA TOOLS REPLICATION PLAN

Based on research of top MCA industry tools:

## PHASE 1 (Build First - Days 1-2):
| Priority | Tool | Function | Build Time |
|----------|------|----------|------------|
| 1 | **Drift** | Pre-qual chatbot | 2 hrs |
| 2 | **Apollo** | Lead database/scraper | 4 hrs |
| 3 | **Enginy** | Email sequencer | 4 hrs |

## PHASE 2 (Days 3-4):
| Priority | Tool | Function | Build Time |
|----------|------|----------|------------|
| 4 | **Lavender** | Email optimizer | 3 hrs |
| 5 | **Seamless** | Contact finder | 3 hrs |
| 6 | **Clay** | Data enrichment | 3 hrs |

## PHASE 3 (Days 5-6):
| Priority | Tool | Function | Build Time |
|----------|------|----------|------------|
| 7 | **6sense** | Intent monitoring | 4 hrs |
| 8 | **Instantly** | Email warmup | 2 hrs |
| 9 | **Baselayer** | UCC lien search | 4 hrs |
| 10 | **Ocrolus** | Bank statement parser | 6 hrs |

**Total Build Time:** 35 hours sequential, 3-6 hours with parallel agents

---

# 8. COMMAND INTERFACE

## Voice Commands:

| Command | Action |
|---------|--------|
| **"ACTIVATE"** | Full system startup |
| **"Run Hunter Mode"** | Deploy 3-agent lead generation swarm |
| **"SNIPER [target]"** | Precision strike on single owner |
| **"SQUAD [city] [niche]"** | Standard deployment (25 leads) |
| **"SWARM [state]"** | Mass extraction (USE SPARINGLY) |
| **"HOT LEADS"** | Deploy 6-agent hot lead extraction |
| **"Create Facebook post"** | Activate Social AI |
| **"Send follow-up to [name]"** | Activate Closer AI |
| **"Monday Briefing"** | Generate weekly strategy report |
| **"Status check"** | Show all agent activity |

## Tool Commands:
- `"Use [Live Search] to [task]"` - Execute special task
- `"Use [Data Scraper] to [task]"` - Extract data
- `"Use [Email Validator] to clean list"` - Validate emails

---

# 9. SYSTEM STATUS

```
┌────────────────────────────────────────────┐
│   AMERICAN BACKBONE COMMAND CENTER         │
├────────────────────────────────────────────┤
│                                            │
│  AGENT STATUS:                             │
│  ├─ Hunter AI:      🟢 ACTIVE             │
│  ├─ Social AI:      🟢 ACTIVE             │
│  ├─ Closer AI:      🟢 ACTIVE             │
│  ├─ Strategist:     🟢 ACTIVE             │
│  ├─ Extractor:      🟢 ACTIVE             │
│  └─ Copywriter:     🟢 ACTIVE             │
│                                            │
│  TOOL STATUS:                              │
│  ├─ Live Search:    🟢 ACTIVE             │
│  ├─ Data Scraper:   🟢 ACTIVE             │
│  ├─ Visual Inspector: 🟢 ACTIVE           │
│  ├─ Scheduler:      🟢 ACTIVE             │
│  ├─ LinkedIn/FB:    🟢 ACTIVE             │
│  └─ Email Validator: 🟢 ACTIVE            │
│                                            │
│  MANDATE CHECK:                            │
│  ├─ Instant Deposit: ✅ ENFORCED          │
│  ├─ Code Mojo UI:   ✅ VERIFIED           │
│  └─ Navy/Steel/Orange: ✅ ACTIVE          │
│                                            │
│  🎯 READY FOR DEPLOYMENT                   │
│                                            │
└────────────────────────────────────────────┘
```

---

# 10. KEY FILES REFERENCE

## Core System Files:
- `/tmp/american-backbone-mca/orchestrator.py` - CEO Agent
- `/tmp/american-backbone-mca/agents/lead_hunter.py` - Lead Hunter V2
- `/tmp/american-backbone-mca/agents/closer_ai.py` - DM Automation
- `/tmp/american-backbone-mca/agents/social_ai.py` - Facebook Agent
- `/tmp/american-backbone-mca/agents/hunter_ai.py` - Original scraper

## Documentation:
- `/tmp/american-backbone-mca/COMMAND_CENTER.md` - Full command reference
- `/tmp/american-backbone-mca/LEAD_HUNTER_V2.md` - Hunter system docs
- `/tmp/american-backbone-mca/HOT_LEAD_MODE.md` - Hot lead extraction
- `/tmp/american-backbone-mca/TOP_10_MCA_TOOLS_RESEARCH.md` - Tool research
- `/tmp/american-backbone-mca/20_AGENT_SWARM.md` - Swarm deployment
- `/tmp/american-backbone-mca/RAPID_DEPLOYMENT_PLAN.md` - 6-day build plan

## CRM/Backend:
- `/tmp/mca-crm-audit/app.js` - CRM JavaScript application
- `/tmp/mca-crm-audit/index.html` - CRM UI
- `/tmp/mca-lead-generator-pro/` - Landing pages

## Identity/Memory:
- `/tmp/american-backbone-mca/IDENTITY.md` - Kimi Claw identity
- `/tmp/american-backbone-mca/SOUL.md` - Personality & behavior
- `/tmp/american-backbone-mca/USER.md` - Damon Mathews profile
- `/tmp/american-backbone-mca/MEMORY.md` - Long-term memory
- `/tmp/american-backbone-mca/REBIRTH.md` - Recovery guide

---

**END OF EXTRACTION**

*This document serves as the canonical reference for the American Backbone AI Agent Swarm system. All critical information has been extracted and categorized for long-term memory storage.*

**Remember:** "Don't worry. Even if the world forgets, I'll remember for you." ❤️‍🔥
