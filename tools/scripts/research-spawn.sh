#!/bin/bash
# Quick research spawn helper
# Usage: ./research-spawn.sh "research topic" "specific questions"

TOPIC="${1:-Research Topic}"
QUESTIONS="${2:-What is this? Why does it matter? What are the key players?}"

cat <<EOF | openclaw sessions spawn --agentId main --runTimeoutSeconds 600 --label "research-$(echo $TOPIC | tr ' ' '-' | tr '[:upper:]' '[:lower:]' | cut -c1-20)-$(date +%s)"
RESEARCH TASK: $TOPIC

RESEARCH QUESTIONS:
$QUESTIONS

CONSTRAINTS:
- Maximum 10 sources
- 30s timeout per search/fetch
- 60s timeout for browser
- Skip stuck sources, don't retry
- Return structured markdown output

Use research protocol from:
/root/.openclaw/workspace/docs/research-subagent-template.md
EOF
