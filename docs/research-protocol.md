# Research Subagent Protocol

## When to Use What

### **Immediate / Main Session** (< 3 min)
- Quick lookups (1-2 searches)
- Known sources (go directly to URL)
- Interactive exploration (you want to steer)

### **Research Subagent** (> 3 min, < 15 min)
- Multi-source research
- Competitor analysis
- Market research
- Tool comparison

### **Async/Cron** (repeating)
- Daily/weekly monitoring
- Scheduled reports

---

## Research Subagent Template

### Spawn Command
```
sessions_spawn(
  task="[RESEARCH TASK] - detailed prompt here",
  agentId="main",
  runTimeoutSeconds=600,  // 10 min hard limit
  label="research-[topic]-[timestamp]"
)
```

### Subagent Behavior Rules
1. **Tool timeouts built-in** (30s search, 60s browser)
2. **Checkpoint every 3 sources** - save intermediate findings
3. **If stuck > 2 min on one source** - skip and note it
4. **Return structured output** (not raw dumps)

### Expected Output Format
```markdown
# Research: [Topic]

## Summary (3 bullets max)
- Key finding 1
- Key finding 2
- Key finding 3

## Sources Analyzed
| Source | Relevance | Notes |
|--------|-----------|-------|
| url1   | High      | Key point |
| url2   | Medium    | Partial info |

## Recommendations
1. Action item 1
2. Action item 2

## Sources That Timed Out (if any)
- [url] - reason
```

---

## Tool Timeout Wrappers

### Search (30s timeout)
```javascript
// searchWithTimeout(query, timeoutMs=30000)
```

### Fetch (30s timeout)  
```javascript
// fetchWithTimeout(url, timeoutMs=30000)
```

### Browser (60s timeout)
```javascript
// browserWithTimeout(url, action, timeoutMs=60000)
```

---

## Chunked Fallback Protocol

If subagent isn't right for the job, use this pattern:

### Phase 1: Discovery (2-3 searches)
- Broad search to map the landscape
- Save top 5 sources
- **Checkpoint**: Present findings, confirm direction

### Phase 2: Deep Dive (top 3 sources)
- Fetch full content
- Extract key insights
- **Checkpoint**: Present analysis, confirm next steps

### Phase 3: Synthesis
- Combine findings
- Form recommendations
- Deliver final output

---

## Failure Recovery

### Subagent Times Out
1. Check what was completed
2. Restart with narrower scope
3. Or switch to chunked main-session approach

### Tool Timeout
1. Log which source failed
2. Continue with remaining sources
3. Report timeouts in output

---

*Created: 2026-03-22*
*Purpose: Prevent research task timeouts*
