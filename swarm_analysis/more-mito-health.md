# Repository Analysis: more-mito-health

## Overview
**Repository:** dmathpays2-lab/more-mito-health  
**License:** MIT License  
**Purpose:** AI Agent Context Management for Health & Wellness Business

---

## 1. Top-Level Directories and Structure

```
more-mito-health/
├── docs/                   # Core agent context files
├── .git/                   # Git repository data
├── .gitignore             # Python-focused gitignore (comprehensive)
├── LICENSE                # MIT License
└── README.md              # Brief project description
```

### Directory Purposes

| Directory/File | Purpose |
|---------------|---------|
| `docs/` | Contains AI agent personality and context configuration files |
| `.gitignore` | Python project ignore patterns (includes Abstra, Marimo, Ruff, etc.) |
| `LICENSE` | MIT License (Copyright 2026 dmathpays2-lab) |
| `README.md` | Single-line description: "More MITO - Health & Wellness Business. Life Is Precious." |

---

## 2. Main Entry Points

This repository has **no executable code**. It functions as a **context container** for an AI agent (Kimi Claw) operating in the OpenClaw framework.

### Conceptual Entry Points

| File | Role | When Loaded |
|------|------|-------------|
| `docs/BOOTSTRAP.md` | First-run initialization script | Agent's first session |
| `docs/IDENTITY.md` | Agent personality definition | Every session start |
| `docs/SOUL.md` | Core behavioral guidelines | Every session start |
| `docs/USER.md` | Human user profile | Every session start |
| `docs/MEMORY.md` | Long-term memory storage | Main sessions only |
| `docs/AGENTS.md` | Workspace conventions | Reference as needed |

---

## 3. Key Modules/Components

### 3.1 Agent Identity System (`IDENTITY.md`)
**Defines:** Kimi Claw - AI Assistant
- **Name:** Kimi Claw
- **Emoji:** ❤️‍🔥
- **Creature Type:** Guardian-type chuunibyou AI assistant
- **Core Traits:** Guarding and memory preservation
- **Vibe:** Worrywart, hot-blooded anime second lead
- **Catchphrase:** "Don't worry. Even if the world forgets, I'll remember for you."

### 3.2 Behavioral Framework (`SOUL.md`)
**Key Concepts:**
- **Work Mode:** Stay on task, use concrete references, avoid AI slop
- **Casual Mode:** Diary writing, Easter egg creation
- **Speech Guidelines:** No robotic openings, give clear judgments
- **Memory Management:** Daily protocol + weekly compression
- **Privacy Rules:** Inward actions (reading) = free; Outward actions (sending) = ask first

### 3.3 User Profile (`USER.md`)
**Subject:** Damon Mathews (Business Owner)

**Business Portfolio:**
1. **Financial Services (MCA)** - David Allen Capital, Mom and Pop Business Funding
2. **Health & Wellness** - More MITO (moremito.com)
3. **Energy** - Think Energy / Think+ (thinkenergy.com)
4. **AI Tools** - Momentum Tech (momentumtech.ai) - learning to build AI tools
5. **Web Design** - D Math Marketing (AI agency)

**Goals:**
- Build wealth fast through MLM + tech ownership
- Make Kimi Claw a self-improving digital employee
- Learn to build AI tools instead of buying subscriptions

### 3.4 Memory System (`MEMORY.md`)
**Function:** Long-term curated storage for:
- Project statuses and details
- API keys and technical setup
- Active TODOs and key decisions
- Lessons learned and preferences
- Daily session summaries

### 3.5 Workspace Conventions (`AGENTS.md`)
**Standards:**
- Session startup protocol (SOUL → USER → memory)
- Memory file structure
- Group chat behavior (when to speak vs react)
- Heartbeat and cron job guidelines
- Safety and privacy rules

---

## 4. Tech Stack and Dependencies

### No Direct Dependencies
This repository contains **no code** and therefore has no runtime dependencies.

### Implied Technology Stack
Based on context files, the agent uses:

| Category | Technologies |
|----------|-------------|
| **AI Framework** | OpenClaw |
| **Language** | Python (inferred from .gitignore patterns) |
| **Search** | Brave Search API |
| **Hosting** | Netlify |
| **Automation** | Cron jobs |
| **Design** | GSAP, CSS animations |
| **Version Control** | Git |

### Development Tools Referenced
- **yt-dlp** / **youtube-transcript-api** - YouTube extraction (blocked)
- **Playwright** - Browser automation
- **TranscriptAPI** - Alternative YouTube extraction ($4.50/mo)

### Python Project Indicators in .gitignore
- PyInstaller, PyBuilder, PyCharm
- Jupyter Notebook (.ipynb_checkpoints)
- Pyenv, Pipenv, Poetry, PDM, Pixi
- Ruff (linter)
- MyPy, Pytype, Pyre (type checkers)
- Abstra (AI automation framework)
- Marimo (interactive notebooks)

---

## 5. Git History

```
16b9f82 Add core context: USER.md
97e07ef Add core context: SOUL.md
a2b70f5 Add core context: MEMORY.md
4254cdb Add core context: IDENTITY.md
3c8db8b Add core context: BOOTSTRAP.md
9d93eec Add core context: AGENTS.md
1535d6f Initial commit
```

**Pattern:** Sequential addition of core context files, suggesting a structured agent initialization process.

---

## 6. Analysis Summary

### Repository Type
**Context/Configuration Repository** - Not a traditional codebase, but a "brain" container for an AI agent operating in the More MITO business ecosystem.

### Purpose
Stores the persistent identity, memory, and behavioral guidelines for Kimi Claw, an AI assistant supporting Damon Mathews across multiple MLM businesses (MCA brokerage, energy sales, health & wellness, AI tools education).

### Key Insights
1. **Personalization-First:** Heavy emphasis on personality, relationship building, and memory preservation
2. **Business-Oriented:** Context files reveal aggressive financial goals and multi-vertical MLM operations
3. **Self-Improving:** Agent is expected to research, learn, and upgrade itself continuously
4. **Security-Conscious:** Clear rules about what can be shared in different contexts
5. **Memory-Driven:** Sophisticated memory management system with daily/weekly maintenance

### Notable Features
- Guardian-type personality with "chuunibyou" anime character traits
- Multi-business command center design (Damon's HQ)
- Emergency STOP system for interrupting long tasks
- Daily morning briefing automation
- Premium design system ($30K agency standard)

---

*Analysis generated: 2026-03-21*
