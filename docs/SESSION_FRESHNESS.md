# Session Freshness Strategy

## Why New Sessions Fix Problems

When you start fresh, you lose:
- **Context bloat** — accumulated tokens slow everything down
- **Ghost subagents** — stuck runs from hours ago still consuming resources  
- **Tool residue** — partial completions, hanging browser tabs
- **Memory pressure** — cached files, embeddings, search indexes

It's like rebooting a computer that's been on too long.

---

## Current Auto-Freshness Features

### ✅ Already Enabled

| Feature | Setting | Effect |
|---------|---------|--------|
| Auto-compaction | `60K tokens` | Summarizes old context automatically |
| Subagent limits | `maxConcurrent: 8` | Caps parallel agents |
| Session limits | `contextTokens: 131072` | Hard cap at 128K |

### 📊 Freshness Monitor

New tool: `tools/scripts/session_freshness.py`
- Tracks estimated tokens, turns, age
- Health score 0-100
- Suggests rotation when <50

---

## When to Rotate (Start Fresh)

### 🔴 **Definitely Rotate**
- Token count >80K (context getting heavy)
- 50+ turns back-and-forth
- 4+ hours in same session
- Just recovered from timeout/crash
- About to start major new project

### 🟡 **Consider Rotating**  
- Response latency increasing
- Tool calls feel sluggish
- Been context-compacted multiple times
- Switching between unrelated tasks

### 🟢 **Stay Put**
- Deep in focused work
- Building on previous context
- Health score >80
- Under 30 turns

---

## Manual Rotation Workflow

When I suggest starting fresh:

```
1. Save state → "Let me commit this to memory..."
2. Summarize → "Quick recap of where we are..."
3. Confirm → "Ready to start fresh?"
4. New session → Context is clean, memory files loaded
```

## Proactive Rotation (Optional)

If you want automatic rotation:

```json
// Add to openclaw.json
"session": {
  "maxTurns": 50,
  "maxAgeMinutes": 240,
  "suggestRotation": true
}
```

Then I'd say: *"We've been at this for 4 hours — want to start fresh before the next task?"*

---

## My Recommendation

**Don't auto-rotate.** Here's why:

1. **Context is valuable** — losing it slows us down
2. **Compaction works** — 60K auto-summary handles most bloat  
3. **You decide** — you know when a task is done better than a script
4. **Freshness ≠ health** — a 100-turn session can be fine if focused

**Better approach:**
- I monitor freshness and **suggest** rotation
- You decide based on where you are in the work
- We rotate at natural breakpoints (task complete, context switch)

---

## What I Track

| Metric | Current | Threshold | Status |
|--------|---------|-----------|--------|
| Tokens | ~25K | 60K compact / 80K warn | 🟢 OK |
| Turns | ~40 | 50 warn / 70 rotate | 🟡 Close |
| Age | ~20min | 4hr warn | 🟢 OK |
| Health Score | 60/100 | <50 rotate | 🟡 Watch |

---

## Quick Commands

```bash
# Check freshness
python3 tools/scripts/session_freshness.py

# Force compaction (rarely needed)
# Happens automatically at 60K tokens

# Start fresh
# Just say "let's start fresh" — I'll wrap up and rotate
```

---

*Bottom line: I'll watch for session bloat and suggest rotation at natural stopping points. You make the call.*
