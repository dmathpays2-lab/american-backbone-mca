# OpenClaw Timeout Prevention Guide

## The Problem

IM runtime dispatch timeouts occur when an operation takes longer than `promptTimeoutMs` (now 10 minutes). When this happens:
1. The gateway kills the run
2. You get "reborn" (session reset)
3. Context is lost

## Root Causes (What Actually Hangs)

Based on logs and patterns, these are the timeout culprits:

### 1. **Browser Operations** ⚠️ HIGHEST RISK
- `browser snapshot` on JS-heavy sites (React, Vue SPAs)
- Waiting for elements that never appear
- Infinite scroll pages
- **Fix**: Always use `timeoutMs` parameter, avoid `act:wait`

### 2. **Web Search + Fetch Chains** ⚠️ HIGH RISK
- `kimi_search` with `include_content=true` on many results
- Sequential fetches of multiple URLs
- **Fix**: Limit results (5-7), use `include_content=false`, fetch selectively

### 3. **Subagents Without Timeouts** ⚠️ HIGH RISK
- Spawned agents that loop or hang
- Research tasks with unbounded scope
- **Fix**: Always set `runTimeoutSeconds` on spawn

### 4. **Git Operations on Large Repos** ⚠️ MEDIUM RISK
- Cloning repos with 1000+ files
- **Fix**: Use shallow clones (`--depth 1`)

### 5. **File Operations on Large Files** ⚠️ LOW RISK
- Reading huge JSONL files
- **Fix**: Use `limit` and `offset` parameters

## Prevention Rules

### Rule 1: Browser Timeout
```javascript
// GOOD — explicit timeout
browser snapshot --timeoutMs 30000

// BAD — can hang forever
browser snapshot
```

### Rule 2: Search Limits
```javascript
// GOOD — bounded results
kimi_search "query" --limit 5

// BAD — could fetch 10+ pages with content
kimi_search "query" --include_content true
```

### Rule 3: Subagent Timeouts
```javascript
// GOOD — hard deadline
sessions_spawn "task" --runTimeoutSeconds 180

// BAD — could run forever
sessions_spawn "task"
```

### Rule 4: Parallel > Sequential
```javascript
// GOOD — parallel (faster, bounded)
Run 3 searches simultaneously with Promise.all

// BAD — sequential (slower, unbounded)
Search → Wait → Fetch → Search → Wait → Fetch...
```

### Rule 5: Tool Timeouts Wrapper
```python
# Use tools/scripts/research_timeouts.py
# All web ops have 30s max, browser 60s max
```

## Current Protections in Place

1. ✅ **Timeout increased**: 5min → 10min
2. ✅ **Health monitor**: Runs every 2min, kills stuck runs >8min
3. ✅ **Tool wrappers**: Research ops have hard 30-60s caps
4. ✅ **Subagent template**: Standardized with 3min timeouts

## What to Do If Timeout Happens

1. **Don't panic** — memory is in GitHub (docs/, memory/)
2. **Check REBIRTH.md** — follow recovery protocol
3. **Review last operation** — what was I doing when it died?
4. **Add protection** — how do I prevent this specific case?

## Quick Checklist Before Long Operations

- [ ] Is this operation bounded (timeout/limit)?
- [ ] Can it be split into smaller chunks?
- [ ] Should this be a subagent with its own timeout?
- [ ] Am I fetching too much content?
- [ ] Is there a faster way to get this data?

---
Last updated: 2026-03-22
