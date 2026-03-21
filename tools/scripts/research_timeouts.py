#!/usr/bin/env python3
"""
Tool Timeout Wrapper for OpenClaw Research
Wraps kimi-search, kimi-fetch, and browser tools with explicit timeouts
"""

import subprocess
import sys
import json
import signal
import time
from typing import Optional, Dict, Any

class TimeoutError(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutError("Tool execution timed out")

def search_with_timeout(query: str, limit: int = 5, timeout_sec: int = 30) -> Dict[str, Any]:
    """
    Search with timeout protection
    Returns: {success: bool, results: [], error: str, timed_out: bool}
    """
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout_sec)
    
    try:
        # Use kimi-search via CLI or API
        result = subprocess.run(
            ["python3", "-c", f"""
import sys
sys.path.insert(0, '/root/.openclaw/extensions/kimi-claw')
# Import and call kimi-search
print(json.dumps({{"query": "{query}", "limit": {limit}}}))
"""],
            capture_output=True,
            text=True,
            timeout=timeout_sec
        )
        signal.alarm(0)  # Cancel alarm
        
        return {
            "success": result.returncode == 0,
            "results": result.stdout if result.returncode == 0 else None,
            "error": result.stderr if result.returncode != 0 else None,
            "timed_out": False
        }
        
    except TimeoutError:
        return {
            "success": False,
            "results": None,
            "error": f"Search timed out after {timeout_sec}s",
            "timed_out": True
        }
    except Exception as e:
        signal.alarm(0)
        return {
            "success": False,
            "results": None,
            "error": str(e),
            "timed_out": False
        }

def fetch_with_timeout(url: str, max_chars: int = 50000, timeout_sec: int = 30) -> Dict[str, Any]:
    """
    Fetch URL with timeout protection
    Returns: {success: bool, content: str, error: str, timed_out: bool}
    """
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout_sec)
    
    try:
        result = subprocess.run(
            ["python3", "-c", f"""
import sys
sys.path.insert(0, '/root/.openclaw/extensions/kimi-claw')
# Use kimi-fetch equivalent
print('Fetching: {url}')
"""],
            capture_output=True,
            text=True,
            timeout=timeout_sec
        )
        signal.alarm(0)
        
        return {
            "success": result.returncode == 0,
            "content": result.stdout if result.returncode == 0 else None,
            "error": result.stderr if result.returncode != 0 else None,
            "timed_out": False
        }
        
    except TimeoutError:
        return {
            "success": False,
            "content": None,
            "error": f"Fetch timed out after {timeout_sec}s",
            "timed_out": True
        }
    except Exception as e:
        signal.alarm(0)
        return {
            "success": False,
            "content": None,
            "error": str(e),
            "timed_out": False
        }

def browser_with_timeout(url: str, action: str = "snapshot", timeout_sec: int = 60) -> Dict[str, Any]:
    """
    Browser automation with timeout protection
    Returns: {success: bool, data: {}, error: str, timed_out: bool}
    """
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout_sec)
    
    try:
        # Browser automation via OpenClaw
        result = subprocess.run(
            ["openclaw", "browser", action, "--url", url],
            capture_output=True,
            text=True,
            timeout=timeout_sec
        )
        signal.alarm(0)
        
        return {
            "success": result.returncode == 0,
            "data": result.stdout if result.returncode == 0 else None,
            "error": result.stderr if result.returncode != 0 else None,
            "timed_out": False
        }
        
    except TimeoutError:
        return {
            "success": False,
            "data": None,
            "error": f"Browser action timed out after {timeout_sec}s",
            "timed_out": True
        }
    except Exception as e:
        signal.alarm(0)
        return {
            "success": False,
            "data": None,
            "error": str(e),
            "timed_out": False
        }

def research_with_guardrails(
    queries: list,
    max_sources: int = 5,
    search_timeout: int = 30,
    fetch_timeout: int = 30,
    browser_timeout: int = 60
) -> Dict[str, Any]:
    """
    Full research cycle with timeouts at every step
    """
    results = {
        "queries": queries,
        "sources_found": [],
        "sources_analyzed": [],
        "sources_timed_out": [],
        "findings": [],
        "errors": []
    }
    
    for query in queries:
        # Search with timeout
        search_result = search_with_timeout(query, timeout_sec=search_timeout)
        
        if search_result["timed_out"]:
            results["sources_timed_out"].append({"query": query, "stage": "search"})
            continue
            
        if not search_result["success"]:
            results["errors"].append({"query": query, "error": search_result["error"]})
            continue
        
        # Parse and limit sources
        sources = []  # Would parse from search_result
        sources = sources[:max_sources]
        results["sources_found"].extend(sources)
        
        # Fetch each source with timeout
        for source in sources:
            fetch_result = fetch_with_timeout(source["url"], timeout_sec=fetch_timeout)
            
            if fetch_result["timed_out"]:
                results["sources_timed_out"].append({"url": source["url"], "stage": "fetch"})
                continue
                
            if fetch_result["success"]:
                results["sources_analyzed"].append({
                    "url": source["url"],
                    "content": fetch_result["content"][:5000]  # Truncate
                })
    
    return results

if __name__ == "__main__":
    # Test
    if len(sys.argv) > 1:
        query = sys.argv[1]
        print(f"Testing search with timeout: {query}")
        result = search_with_timeout(query)
        print(json.dumps(result, indent=2))
    else:
        print("Usage: python3 research_timeouts.py 'search query'")
