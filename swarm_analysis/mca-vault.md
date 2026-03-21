# MCA-Vault Repository Analysis

**Repository:** dmathpays2-lab/mca-vault  
**Purpose:** AI Agent Swarm for MCA (Merchant Cash Advance) Lead Generation  
**Analysis Date:** 2026-03-21  

---

## 1. Top-Level Directories and Their Purpose

| Directory | Purpose |
|-----------|---------|
| `agents/` | Core AI agent implementations (Python) - Hunter AI, Social AI, Closer AI |
| `api/` | Vercel serverless API endpoint (`index.py`) |
| `apps/` | Contains `blink-clone/` - Full-stack Node.js backend API |
| `agency/` | Business model documentation and agency strategy |
| `docs/` | Documentation files (USER.md, MEMORY.md, AGENTS.md, etc.) |
| `scripts/` | Utility scripts for deployment, migration, and automation |
| `skills/` | OpenClaw skill definitions (lead-hunter with config.json) |
| `research/` | Research documents on MCA tools, YouTube extraction, competitor analysis |
| `planning/` | Business planning documents (kimi-claw automation/business plans) |
| `swarm_deployment/` | Multi-agent swarm deployment scripts and status tracking |
| `memory/` | Working memory storage |
| `conversations/` | Conversation archives |
| `strategy/` | Strategy documents |
| `config/` | Configuration files |
| `.backup/` | Backup of core identity and agent files |
| `bin/` | Binary/executable scripts (hunter launcher) |

---

## 2. Main Entry Points

### Python Agents
| Entry Point | Description |
|-------------|-------------|
| `orchestrator.py` | **Main orchestrator** - CEO agent that coordinates all 3 AI agents |
| `agents/hunter_ai.py` | Lead generation agent - scrapes Yelp, Google Maps for businesses |
| `agents/social_ai.py` | Facebook infiltration agent - posts, monitors groups, engages |
| `agents/closer_ai.py` | DM automation agent - sends closing sequences, follows up |
| `agents/lead_hunter.py` | Refined lead hunter with extraction modes (SNIPER/SQUAD/SWARM) |

### API & Backend
| Entry Point | Description |
|-------------|-------------|
| `api/index.py` | Vercel serverless API - health check and lead submission endpoint |
| `apps/blink-clone/backend/server.js` | Node.js/Express API with auth, billing, forms, webhooks |

### Scripts
| Script | Purpose |
|--------|---------|
| `scripts/hunter-swarm.sh` | Hunter swarm deployment shell script |
| `scripts/setup_github_repos.py` | GitHub repository setup automation |
| `swarm_deployment/deploy_20_agent_swarm.py` | Multi-agent swarm deployment |
| `skills/lead-hunter/run.sh` | OpenClaw skill launcher for lead hunting |

---

## 3. Key Modules/Components

### Agent Architecture
```
┌─────────────────────────────────────────────────────────────┐
│  AMERICAN BACKBONE ORCHESTRATOR (orchestrator.py)          │
│  - CEO Agent that coordinates all operations                │
└──────────────────┬──────────────────────────────────────────┘
                   │
       ┌───────────┼───────────┐
       ▼           ▼           ▼
┌──────────┐ ┌──────────┐ ┌──────────┐
│ HUNTER   │ │ SOCIAL   │ │ CLOSER   │
│ AI       │ │ AI       │ │ AI       │
├──────────┤ ├──────────┤ ├──────────┤
│- Yelp    │ │- Facebook│ │- DMs     │
│ scraping │ │ posts    │ │- Follow- │
│- Google  │ │- Group   │ │  ups     │
│ Maps     │ │ monitor  │ │- Closing │
│- Revenue │ │- Auto-   │ │ scripts  │
│ estimates│ │ response │ │- Booking │
│- Lead    │ │- Content │ │ calls    │
│ scoring  │ │ calendar │ │          │
└──────────┘ └──────────┘ └──────────┘
```

### Core Components

#### Hunter AI (`agents/hunter_ai.py`)
- **Purpose:** Find qualified business owners needing MCA funding
- **Targets:** Construction, Trucking, Motels
- **Qualification Criteria:**
  - $15K+ monthly revenue
  - 500+ FICO score
  - 6+ months in business
- **Data Sources:** Yelp, Google Maps, LinkedIn, Hunter.io
- **Lead Scoring:** 0-100 score based on revenue, business age, industry, contact quality

#### Social AI (`agents/social_ai.py`)
- **Purpose:** Facebook infiltration and engagement
- **Post Types:**
  - "UNSTOPPABLE" posts (red background style)
  - Opinion hooks (bypass spam filters)
  - Search & rescue comments
  - Value authority posts
- **Monitoring:** 15+ Facebook groups for trigger keywords
- **Keywords:** "repair costs", "cash flow", "slow paying", "waiting on check"
- **Daily Output:** 12 posts (4 per niche)

#### Closer AI (`agents/closer_ai.py`)
- **Purpose:** DM automation and closing sequences
- **Sequence:** 7-day automated follow-up
  - Day 0: Initial DM with strategy guide
  - Day 1: Check if received
  - Day 2: Social proof + soft CTA
  - Day 4: Value nurture
  - Day 7: Final follow-up
- **Objection Handlers:** Price, credit, timing, interest
- **Daily Output:** 80 DMs/day

#### Lead Hunter v2 (`agents/lead_hunter.py`)
- **Extraction Modes:**
  - `SNIPER`: 1 high-quality lead
  - `SQUAD`: 25 leads (default)
  - `SWARM`: 100+ leads
- **Filters:** 4 stars or less, new ownership signals
- **Targets:** Box Truck, Roofing/Solar, Motels

### Blink Clone Backend (`apps/blink-clone/backend/`)
- **Framework:** Node.js/Express
- **Features:**
  - Authentication (JWT + bcrypt)
  - Stripe billing integration
  - AI routes (OpenAI integration)
  - Forms and webhooks
  - PostgreSQL database
  - Rate limiting (rate-limiter-flexible)

---

## 4. Tech Stack and Dependencies

### Python Stack
| Component | Version/Type |
|-----------|--------------|
| Language | Python 3.x |
| HTTP Requests | `requests>=2.31.0` |
| Core Libraries | json, os, datetime, pathlib |

### Node.js Stack (Blink Clone)
| Package | Version | Purpose |
|---------|---------|---------|
| express | ^4.18.2 | Web framework |
| pg | ^8.11.0 | PostgreSQL client |
| bcrypt | ^5.1.0 | Password hashing |
| jsonwebtoken | ^9.0.1 | JWT authentication |
| cors | ^2.8.5 | CORS middleware |
| dotenv | ^16.3.1 | Environment variables |
| helmet | ^7.0.0 | Security headers |
| openai | ^4.0.0 | OpenAI API integration |
| stripe | ^12.0.0 | Payment processing |
| uuid | ^9.0.0 | UUID generation |
| validator | ^13.9.0 | Input validation |
| rate-limiter-flexible | ^2.4.2 | Rate limiting |

### Deployment & Infrastructure
| Service | Purpose |
|---------|---------|
| Vercel | Serverless API hosting |
| GitHub | Source control |
| Apify | Web scraping (MCP configured) |
| OpenAI | AI content generation |
| PostgreSQL | Database (Blink clone) |
| Stripe | Payment processing |

### MCP Integration
```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com",
      "headers": {
        "Authorization": "Bearer apify_api_..."
      }
    }
  }
}
```

---

## 5. Key Configuration Files

| File | Purpose |
|------|---------|
| `vercel.json` | Vercel deployment configuration |
| `mcp-config.json` | MCP server configuration (Apify) |
| `requirements.txt` | Python dependencies |
| `skills/lead-hunter/config.json` | OpenClaw skill configuration |

---

## 6. Documentation Files

| File | Description |
|------|-------------|
| `README.md` | Main project documentation (comprehensive) |
| `MASTERMIND.md` | System mastermind overview |
| `INTEGRATION_PLAN.md` | Integration roadmap |
| `INTEGRATION_COMPLETE.md` | Integration completion status |
| `RAPID_DEPLOYMENT_PLAN.md` | Quick deployment guide |
| `100_AGENT_THEORY.md` | Theory behind 100-agent system |
| `HOT_LEAD_MODE.md` | Hot lead identification strategy |
| `IMPROVEMENT_SYSTEM.md` | Continuous improvement framework |
| `TOP_10_MCA_TOOLS_RESEARCH.md` | Market research |
| `SYSTEM_SUMMARY.md` | System overview |
| `SUPER_AGENT_STATUS.md` | Agent status tracking |
| `AGENTS.md` | Agent configuration |
| `SOUL.md` | System identity |
| `IDENTITY.md` | Brand identity |
| `MEMORY.md` | Working memory |
| `HEARTBEAT.md` | System heartbeat/monitoring |
| `FEW_HOURS_ANALYSIS.md` | Time-boxed analysis results |

---

## 7. Business Context

**American Backbone** is an MCA (Merchant Cash Advance) lead generation system that:
- Targets trucking, construction, and motel businesses
- Generates 60 qualified leads/day
- Posts 12x/day on Facebook
- Sends 80 DMs/day with automated follow-ups
- Aims for 15-25 deals/month at $3K average commission

**Cost Comparison:**
- Human Team: $12,000/month
- AI Agents: $450/month
- **Savings: $11,550/month**

---

## 8. File Structure Summary

```
mca-vault/
├── agents/                 # AI agent implementations
│   ├── hunter_ai.py       # Lead generation
│   ├── lead_hunter.py     # Refined hunter v2
│   ├── social_ai.py       # Facebook automation
│   └── closer_ai.py       # DM automation
├── api/                   # Vercel serverless API
│   └── index.py
├── apps/                  # Full-stack applications
│   └── blink-clone/       # Node.js backend
│       └── backend/
│           ├── server.js
│           ├── package.json
│           └── routes/
├── scripts/               # Utility scripts
├── skills/                # OpenClaw skill definitions
├── swarm_deployment/      # Multi-agent deployment
├── docs/                  # Documentation
├── research/              # Research documents
├── planning/              # Business planning
├── agency/                # Agency business model
└── orchestrator.py        # Main entry point
```

---

*Analysis generated for swarm repository understanding.*
