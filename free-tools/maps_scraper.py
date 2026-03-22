#!/usr/bin/env python3
"""
FREE Google Maps Scraper for MCA Leads
Uses Tandem Browser + Python (no Apify needed)
"""

import json
import time
import re
from urllib.parse import quote_plus

# Configuration
TANDEM_API = "http://127.0.0.1:8765"

def get_token():
    with open('/root/.tandem/api-token', 'r') as f:
        return f.read().strip()

def search_google_maps(city, industry, max_results=50):
    """
    Search Google Maps for businesses
    Example: search_google_maps("Phoenix AZ", "restaurants", 50)
    """
    token = get_token()
    
    # Build search URL
    query = quote_plus(f"{industry} in {city}")
    url = f"https://www.google.com/maps/search/{query}"
    
    print(f"🔍 Searching: {industry} in {city}")
    print(f"URL: {url}")
    
    # Open in Tandem
    import requests
    headers = {"Authorization": f"Bearer {token}"}
    
    # Open new tab
    resp = requests.post(
        f"{TANDEM_API}/tabs/open",
        headers=headers,
        json={"url": url, "focus": True}
    )
    tab = resp.json().get('tab', {})
    tab_id = tab.get('id')
    
    print(f"✅ Tab opened: {tab_id}")
    
    # Wait for results to load
    time.sleep(5)
    
    # Get snapshot
    snapshot_resp = requests.get(
        f"{TANDEM_API}/snapshot?compact=false",
        headers=headers
    )
    
    # Parse businesses from snapshot
    snapshot = snapshot_resp.json().get('snapshot', '')
    
    # Extract business listings (this is basic - will need refinement)
    businesses = parse_businesses_from_snapshot(snapshot, max_results)
    
    print(f"📊 Found {len(businesses)} businesses")
    
    return businesses

def parse_businesses_from_snapshot(snapshot, max_results):
    """
    Parse business listings from Tandem snapshot
    This is a basic parser - will need iteration based on actual snapshot structure
    """
    businesses = []
    lines = snapshot.split('\n')
    
    current_business = {}
    
    for line in lines[:2000]:  # Limit to avoid timeout
        # Look for business name patterns
        if 'heading' in line and 'level=' in line:
            name_match = re.search(r'StaticText "([^"]+)"', line)
            if name_match:
                name = name_match.group(1)
                if name and len(name) > 2 and not any(x in name.lower() for x in ['google', 'maps', 'search', 'filter']):
                    current_business = {'name': name}
        
        # Look for phone numbers
        if re.search(r'\(\d{3}\)\s*\d{3}-\d{4}', line) or re.search(r'\d{3}-\d{3}-\d{4}', line):
            phone = re.search(r'[\(\)\d\s\-]{10,}', line)
            if phone and current_business:
                current_business['phone'] = phone.group(0).strip()
        
        # Look for addresses (simplified)
        if re.search(r'\d+\s+[\w\s]+(?:St|Ave|Rd|Dr|Blvd|Ln|Way)', line, re.IGNORECASE):
            if current_business and 'address' not in current_business:
                addr_match = re.search(r'StaticText "([^"]+)"', line)
                if addr_match:
                    current_business['address'] = addr_match.group(1)
        
        # Save complete business
        if current_business and len(current_business) >= 2:
            if current_business not in businesses:
                businesses.append(current_business.copy())
                if len(businesses) >= max_results:
                    break
            current_business = {}
    
    return businesses

def save_leads(leads, filename):
    """Save leads to JSON file"""
    with open(filename, 'w') as f:
        json.dump(leads, f, indent=2)
    print(f"💾 Saved {len(leads)} leads to {filename}")

def main():
    import sys
    
    if len(sys.argv) < 3:
        print("Usage: maps_scraper.py <city> <industry> [max_results]")
        print("Example: maps_scraper.py 'Phoenix AZ' restaurants 50")
        sys.exit(1)
    
    city = sys.argv[1]
    industry = sys.argv[2]
    max_results = int(sys.argv[3]) if len(sys.argv) > 3 else 50
    
    leads = search_google_maps(city, industry, max_results)
    
    # Save to file
    filename = f"/root/.openclaw/workspace/leads/{industry.replace(' ', '_')}_{city.replace(' ', '_').replace(',', '')}.json"
    
    # Create leads directory if needed
    import os
    os.makedirs('/root/.openclaw/workspace/leads', exist_ok=True)
    
    save_leads(leads, filename)
    
    # Also save to MCP memory
    print(f"\n📋 First 5 leads:")
    for i, lead in enumerate(leads[:5], 1):
        print(f"{i}. {lead.get('name', 'N/A')} - {lead.get('phone', 'No phone')}")

if __name__ == "__main__":
    main()
