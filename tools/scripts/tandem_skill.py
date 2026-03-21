#!/usr/bin/env python3
"""
Tandem Browser Skill for OpenClaw
Wraps the Tandem Browser local API for seamless integration

Author: Kimi Claw for Damon Mathews
"""

import os
import json
import requests
from typing import Dict, List, Optional, Any
from urllib.parse import urljoin

class TandemBrowser:
    """
    Tandem Browser API Client for OpenClaw
    
    Provides human-in-the-loop browsing with 250+ API endpoints
    for tabs, navigation, snapshots, automation, and more.
    """
    
    def __init__(self, base_url: str = "http://127.0.0.1:8765", token: Optional[str] = None):
        """
        Initialize Tandem Browser client
        
        Args:
            base_url: Tandem API base URL (default: http://127.0.0.1:8765)
            token: API token (if None, reads from ~/.tandem/api-token)
        """
        self.base_url = base_url.rstrip('/')
        
        if token is None:
            token_path = os.path.expanduser("~/.tandem/api-token")
            if os.path.exists(token_path):
                with open(token_path) as f:
                    token = f.read().strip()
            else:
                raise RuntimeError(
                    f"Tandem API token not found at {token_path}. "
                    "Please run install-tandem.sh first."
                )
        
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
    
    def _request(self, method: str, endpoint: str, **kwargs) -> Any:
        """Make HTTP request to Tandem API"""
        url = urljoin(self.base_url + "/", endpoint.lstrip('/'))
        
        # Add headers if not provided
        if 'headers' not in kwargs:
            kwargs['headers'] = self.headers
        
        try:
            response = requests.request(method, url, timeout=30, **kwargs)
            response.raise_for_status()
            
            # Return JSON if possible, else text
            if response.headers.get('content-type', '').startswith('application/json'):
                return response.json()
            return response.text
            
        except requests.exceptions.ConnectionError:
            raise RuntimeError(
                f"Cannot connect to Tandem at {self.base_url}. "
                "Make sure Tandem Browser is running (./start-tandem.sh)"
            )
        except requests.exceptions.HTTPError as e:
            if response.status_code == 401:
                raise RuntimeError("Tandem API token rejected. Check ~/.tandem/api-token")
            raise RuntimeError(f"Tandem API error: {e}")
    
    # ==================== Status & Info ====================
    
    def status(self) -> Dict:
        """Get Tandem browser status"""
        return self._request("GET", "/status")
    
    def is_running(self) -> bool:
        """Check if Tandem is running"""
        try:
            self.status()
            return True
        except:
            return False
    
    # ==================== Tab Management ====================
    
    def list_tabs(self) -> List[Dict]:
        """List all open tabs"""
        return self._request("GET", "/tabs/list")
    
    def get_tab(self, tab_id: str) -> Dict:
        """Get tab details by ID"""
        return self._request("GET", f"/tabs/{tab_id}")
    
    def open_tab(self, url: str, focus: bool = True) -> Dict:
        """
        Open a new tab
        
        Args:
            url: URL to navigate to
            focus: Whether to focus the new tab
        """
        return self._request("POST", "/tabs/open", json={"url": url, "focus": focus})
    
    def close_tab(self, tab_id: str) -> Dict:
        """Close a tab by ID"""
        return self._request("POST", f"/tabs/{tab_id}/close")
    
    def navigate_tab(self, tab_id: str, url: str) -> Dict:
        """Navigate a tab to a new URL"""
        return self._request("POST", f"/tabs/{tab_id}/navigate", json={"url": url})
    
    # ==================== Content Extraction ====================
    
    def snapshot(self, compact: bool = True) -> Dict:
        """
        Get full page snapshot
        
        Args:
            compact: Return compact JSON (recommended)
        """
        return self._request("GET", "/snapshot", params={"compact": str(compact).lower()})
    
    def find(self, by: str, value: str) -> List[Dict]:
        """
        Find elements on the page
        
        Args:
            by: Search method - "text", "selector", "aria"
            value: Search value
        """
        return self._request("POST", "/find", json={"by": by, "value": value})
    
    # ==================== Automation ====================
    
    def click(self, element_id: str, tab_id: Optional[str] = None) -> Dict:
        """Click an element"""
        data = {"elementId": element_id}
        if tab_id:
            data["tabId"] = tab_id
        return self._request("POST", "/action/click", json=data)
    
    def type_text(self, element_id: str, text: str, tab_id: Optional[str] = None) -> Dict:
        """Type text into an element"""
        data = {"elementId": element_id, "text": text}
        if tab_id:
            data["tabId"] = tab_id
        return self._request("POST", "/action/type", json=data)
    
    def fetch_session(self, tab_id: str, url: str, method: str = "GET", 
                      body: Optional[Dict] = None) -> Dict:
        """
        Fetch with session context (for authenticated APIs)
        
        Args:
            tab_id: Tab ID to use session from
            url: URL to fetch (can be relative)
            method: HTTP method
            body: Request body for POST/PUT
        """
        data = {"tabId": tab_id, "url": url, "method": method}
        if body:
            data["body"] = body
        return self._request("POST", "/sessions/fetch", json=data)
    
    # ==================== High-Level Workflows ====================
    
    def research_url(self, url: str, wait_for_load: bool = True) -> Dict:
        """
        Open URL and extract full content - perfect for YouTube, SPAs, etc.
        
        Args:
            url: URL to research
            wait_for_load: Whether to wait for page load
        """
        # Open tab
        tab = self.open_tab(url, focus=True)
        tab_id = tab.get("id")
        
        # Wait a bit for SPA rendering (optional)
        if wait_for_load:
            import time
            time.sleep(3)
        
        # Get snapshot
        snapshot = self.snapshot(compact=True)
        
        return {
            "tab_id": tab_id,
            "url": url,
            "snapshot": snapshot,
            "title": snapshot.get("title", ""),
            "text_content": snapshot.get("text", "")
        }
    
    def extract_youtube_info(self, video_url: str) -> Dict:
        """
        Extract YouTube video information
        Works where cloud scraping fails!
        """
        result = self.research_url(video_url)
        
        # Try to find video title and description
        title_elements = self.find("selector", "h1")
        desc_elements = self.find("selector", "#description-inline-expander")
        
        return {
            "url": video_url,
            "title": title_elements[0].get("text", "") if title_elements else "",
            "description": desc_elements[0].get("text", "") if desc_elements else "",
            "page_text": result["text_content"],
            "tab_id": result["tab_id"]
        }
    
    def multi_tab_research(self, urls: List[str]) -> List[Dict]:
        """
        Open multiple URLs in tabs and extract summaries
        Perfect for competitive research, news monitoring, etc.
        """
        results = []
        
        for url in urls:
            try:
                result = self.research_url(url, wait_for_load=False)
                results.append(result)
            except Exception as e:
                results.append({"url": url, "error": str(e)})
        
        return results


# ==================== CLI Interface ====================

def main():
    """CLI interface for testing Tandem"""
    import sys
    import argparse
    
    parser = argparse.ArgumentParser(description="Tandem Browser Skill for OpenClaw")
    parser.add_argument("--status", action="store_true", help="Check Tandem status")
    parser.add_argument("--tabs", action="store_true", help="List all tabs")
    parser.add_argument("--open", metavar="URL", help="Open URL in new tab")
    parser.add_argument("--snapshot", action="store_true", help="Get page snapshot")
    parser.add_argument("--research", metavar="URL", help="Research URL and extract content")
    parser.add_argument("--youtube", metavar="URL", help="Extract YouTube video info")
    
    args = parser.parse_args()
    
    try:
        tandem = TandemBrowser()
        
        if args.status:
            status = tandem.status()
            print(json.dumps(status, indent=2))
        
        elif args.tabs:
            tabs = tandem.list_tabs()
            print(f"Active tabs: {len(tabs)}")
            for tab in tabs:
                print(f"  [{tab.get('id')}] {tab.get('title', 'Untitled')}")
                print(f"      {tab.get('url', '')}")
        
        elif args.open:
            result = tandem.open_tab(args.open)
            print(f"Opened: {result.get('url')}")
            print(f"Tab ID: {result.get('id')}")
        
        elif args.snapshot:
            snapshot = tandem.snapshot()
            print(json.dumps(snapshot, indent=2)[:2000])  # Truncate for readability
        
        elif args.research:
            result = tandem.research_url(args.research)
            print(f"Title: {result['title']}")
            print(f"Content preview: {result['text_content'][:500]}...")
        
        elif args.youtube:
            info = tandem.extract_youtube_info(args.youtube)
            print(f"Video: {info['title']}")
            print(f"Description: {info['description'][:300]}...")
        
        else:
            parser.print_help()
    
    except RuntimeError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
