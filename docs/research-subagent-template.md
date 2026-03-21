# Research Subagent Template

## Purpose
Standardized research subagent that never hangs, always reports back, and handles timeouts gracefully.

## Spawn Pattern

```javascript
// From main session:
sessions_spawn({
  task: `RESEARCH TASK: [topic]

RESEARCH QUESTIONS:
1. [Specific question 1]
2. [Specific question 2]
3. [Specific question 3]

CONSTRAINTS:
- Maximum 10 sources total
- Skip any source that takes >30s to load
- If stuck on one source >2 min, skip it
- Return structured output only

OUTPUT FORMAT:
Use the template in /root/.openclaw/workspace/docs/research-output-template.md

TIMEOUT: 10 minutes hard limit`,
  agentId: "main",
  runTimeoutSeconds: 600,
  label: "research-[topic]-" + Date.now()
})
```

## Subagent Internal Protocol

When spawned as a research subagent:

1. **Acknowledge receipt** within 30 seconds
2. **Plan the research** (2-3 search queries max)
3. **Execute with timeouts:**
   - Search: 30s timeout per query
   - Fetch: 30s timeout per URL
   - Browser: 60s timeout per action
4. **Checkpoint every 3 sources**
5. **Return structured output** (never raw dumps)

## Timeout Handling

### Search Times Out
- Log it: "Search for '[query]' timed out after 30s"
- Try alternative query
- If 2 searches timeout, skip to synthesis with available data

### Fetch Times Out
- Log it: "Source [url] timed out, skipping"
- Continue to next source
- Don't retry same URL

### Browser Times Out
- Log it: "Browser automation timed out on [url]"
- Try simpler action (snapshot instead of full interaction)
- If still failing, skip site

## Output Template

```markdown
# Research Results: [Topic]

## Executive Summary
[3-5 sentences max with key findings]

## Detailed Findings

### [Question 1]
**Answer:** [Direct answer]
**Sources:** [url1], [url2]
**Confidence:** High/Medium/Low

### [Question 2]
...

## Sources Analyzed
| Source | Type | Status | Key Info |
|--------|------|--------|----------|
| url1 | Article | Success | Main finding |
| url2 | Report | Timeout | N/A |

## Failed/Timed Out
- [url] - Fetch timeout after 30s
- [search query] - No results in 30s

## Recommendations
1. [Actionable recommendation 1]
2. [Actionable recommendation 2]

## Data Quality Notes
- [Any limitations in the research]
- [Sources that couldn't be accessed]
```

## Error Recovery

### If subagent times out completely:
Main session receives timeout notification. Options:
1. Restart subagent with narrower scope
2. Switch to chunked main-session research
3. Accept partial results

### If subagent crashes:
Main session receives error. Check:
1. Logs in subagent session
2. Restart with different approach
3. Escalate to main session for manual handling

---

*Template version: 1.0*
*Use for all research tasks > 3 minutes*
