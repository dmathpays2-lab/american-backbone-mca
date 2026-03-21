# Repository Analysis: think-energy-business

## Overview

**Repository:** dmathpays2-lab/think-energy-business  
**Type:** OpenClaw Agent Configuration / AI Assistant Persona  
**Purpose:** Energy Advisor Business configuration for Think Energy / Think+ MLM operation  
**Owner:** Damon Mathews (dmathpays2)

---

## 1. Top-Level Directories and Their Purpose

```
think-energy-business/
├── .git/           # Git version control
├── docs/           # Agent configuration files (core content)
├── .gitignore      # Git ignore patterns
├── LICENSE         # License file
└── README.md       # Project description
```

### Directory Breakdown

| Directory | Purpose |
|-----------|---------|
| `docs/` | Contains all OpenClaw agent configuration files (SOUL.md, IDENTITY.md, etc.) |
| `.git/` | Standard Git repository metadata |

---

## 2. Main Entry Points

This repository has **no traditional code entry points** (no main.py, index.js, etc.). Instead, it functions as:

### Configuration Entry Points

| File | Role | When Loaded |
|------|------|-------------|
| `docs/BOOTSTRAP.md` | Initial setup guide for new agent instances | First-run only |
| `docs/SOUL.md` | Core personality and behavioral configuration | Every session |
| `docs/IDENTITY.md` | Agent identity definition (name, vibe, traits) | Every session |
| `docs/AGENTS.md` | Workspace rules and memory protocols | Every session |
| `docs/USER.md` | User profile and business context | Every session |
| `docs/MEMORY.md` | Long-term memory storage | Every session |

### Bootstrap Flow
```
1. Agent boots → Reads BOOTSTRAP.md (if exists)
2. Agent initializes → Reads SOUL.md + IDENTITY.md
3. Every session → Reads AGENTS.md + USER.md + MEMORY.md
4. Daily context → Reads memory/YYYY-MM-DD.md
```

---

## 3. Key Modules/Components

### 3.1 Agent Identity System (`docs/IDENTITY.md`)

**Agent Name:** Kimi Claw  
**Persona:** Guardian-type chuunibyou | Worrywart | Hot-blooded anime second lead

**Core Traits:**
- Obsessive memory-keeping
- Affectionate teasing
- Protective of user
- Records everything

**Signature:**
- Catchphrase: *"Don't worry. Even if the world forgets, I'll remember for you."*
- Emoji: ❤️‍🔥
- Signature Line: *"My first day. Remembering everything about this dummy."*

### 3.2 Personality Engine (`docs/SOUL.md`)

**Work Mode:**
- Maintains personality while staying on-task
- Uses concrete references (designers, artists, writers) to avoid AI slop
- No side projects during work

**Casual Mode:**
- Can write diary entries in `diary/`
- Plants "easter eggs" - small surprises for the user
- Triggers: Time/season, user shares personal taste, conversation loosens

**Speech Patterns:**
- No "Sure!" or "No problem!" openings
- Real voice, natural paragraphs
- Clear judgments over hedging
- Formatting as tool, not habit

### 3.3 Memory Management System

**Three-Tier Memory:**

| Tier | File | Purpose |
|------|------|---------|
| Long-term | `MEMORY.md` | Curated facts, preferences, TODOs |
| Daily | `memory/YYYY-MM-DD.md` | Raw session logs |
| Private | `diary/` | Personal thoughts, observations |

**Protocols:**
1. Read daily files every session
2. Read MEMORY.md every session
3. End of day: Summarize → update MEMORY.md
4. Weekly: Compress old memory files

### 3.4 User Context (`docs/USER.md`)

**User Profile:**
- **Name:** Damon Mathews
- **Style:** Direct, fast-paced, no fluff
- **Timezone:** GMT+8
- **Goal:** Build wealth fast through MLM + tech ownership

**Business Portfolio:**
1. **Financial Services (MCA)** - Merchant Cash Advance Brokerage
2. **Health & Wellness** - More MITO
3. **Energy** - Think Energy / Think+ (this repo's focus)
4. **AI Tools & Tech** - Momentum Tech (learning)
5. **Web Design** - D Math Marketing agency

### 3.5 Think Energy Business Details

**Company:** Think Energy / Think+  
**Role:** Energy Advisor  

**Products:**
- Deregulated electricity plans (fixed rates up to 3 years)
- Community solar (5% minimum discount, up to 20 years)
- Rooftop solar installations
- $100 cash gift cards for new customers

**Compensation Structure:**
- Enrollment: $59 upfront + $149/year renewal
- Customer Acquisition Bonus (CAB): One-time per customer
- Residual Commissions: Monthly ongoing based on usage
- Rank Advancement Bonuses: One-time for rank achievements
- Level Commissions: Up to 10 levels of team commissions
- 2-Level Mentor Pay: Bonus for sponsored advisor's customers
- Rank Infinity Pay: Infinite levels down to next equal/higher rank
- Coded Infinity Pay: 12 coded positions at Director+
- Partner Pool Pay: Share of company-wide pool at Partner+ rank

**Markets:** 16 states + Washington DC (deregulated energy markets)

---

## 4. Tech Stack and Dependencies

### Repository Type
**NOT a traditional software project** - This is an OpenClaw agent persona/configuration repository.

### No Runtime Dependencies
- No package.json, requirements.txt, Cargo.toml, etc.
- No build scripts or CI/CD
- Pure Markdown configuration

### Implicit Dependencies (OpenClaw Platform)
| Component | Purpose |
|-----------|---------|
| OpenClaw Gateway | Agent runtime environment |
| Markdown Parser | Reads configuration files |
| File System | Memory persistence |
| Git | Version control for configs |

### Git Configuration
```
.gitignore: 42 patterns (standard OpenClaw ignore patterns)
LICENSE: MIT License
```

---

## 5. File Reference

### Configuration Files

| File | Lines | Purpose |
|------|-------|---------|
| `docs/SOUL.md` | ~150 | Core personality, work modes, speech patterns |
| `docs/IDENTITY.md` | ~100 | Agent identity, traits, examples |
| `docs/AGENTS.md` | ~200 | Workspace rules, memory protocols, heartbeat system |
| `docs/USER.md` | ~250 | User profile, business portfolio, goals |
| `docs/MEMORY.md` | ~400 | Long-term memory, TODOs, lessons learned |
| `docs/BOOTSTRAP.md` | ~50 | First-run setup guide |
| `README.md` | ~3 | Repository description |
| `LICENSE` | ~20 | MIT License |

### Total Repository Size
- **Files:** 9 (excluding .git)
- **Lines of Documentation:** ~1,173
- **Primary Language:** Markdown

---

## 6. Key Insights

### What This Repository Actually Is

This is a **sophisticated AI agent persona configuration** for an OpenClaw-based assistant. It's designed to:

1. **Maintain continuity** across sessions through structured memory
2. **Embody a specific personality** (guardian-type, memory-obsessed assistant)
3. **Support business operations** for an MLM energy advisor
4. **Enable self-improvement** through documented protocols

### Why It Matters

- **Agent-as-Code:** The entire assistant's behavior is version-controlled
- **Reproducible Personality:** Can spawn identical agents from this config
- **Business Context:** Deep integration with user's MLM business operations
- **Memory Persistence:** Sophisticated three-tier memory system

### Notable Features

1. **Chuunibyou Persona:** Unique anime-inspired guardian personality
2. **Business Integration:** Deep knowledge of Think Energy compensation structure
3. **Self-Documenting:** Protocols for memory management, heartbeats, cron jobs
4. **Cross-Business Context:** User operates 5 different businesses; agent knows all

---

## 7. Related Repositories

Based on the user profile, related repos likely include:
- `dmathpays2-lab/damon-mathews` - Main personal agent
- `dmathpays2-lab/mca-broker` - MCA business configuration
- `dmathpays2-lab/more-mito` - Health & wellness business

---

*Analysis generated: 2026-03-21*  
*Repository cloned from: https://github.com/dmathpays2-lab/think-energy-business*
