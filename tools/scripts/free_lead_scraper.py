#!/usr/bin/env python3
"""
Free B2B Lead Scraper for MCA
Replaces Apollo.io paid API with free sources
"""

import json
import time
from typing import List, Dict, Optional

class FreeLeadScraper:
    """
    Aggregates free B2B data sources for MCA lead generation
    """
    
    def __init__(self):
        self.results = []
        self.sources_used = []
    
    def search_google_places(self, industry: str, location: str, max_results: int = 20) -> List[Dict]:
        """
        Use Google Places API (you already have this configured)
        Target: trucking companies, construction, restaurants, motels
        """
        # This calls your existing Google Places setup
        # Returns: business name, address, phone, website
        pass
    
    def scrape_yelp(self, category: str, location: str, max_results: int = 20) -> List[Dict]:
        """
        Scrape Yelp for local businesses
        Uses Scrapling to bypass bot detection
        """
        # Scrape business listings
        # Extract: name, phone, address, owner name (if available)
        pass
    
    def scrape_linkedin_company(self, company_name: str) -> Dict:
        """
        Use Tandem Browser to scrape LinkedIn company page
        Gets: employee count, industry, location, decision makers
        """
        # Tandem browser automation
        # Navigate to LinkedIn, extract company data
        pass
    
    def find_email_hunter_pattern(self, domain: str, first_name: str, last_name: str) -> Optional[str]:
        """
        Use Hunter.io free API (50 requests/month)
        Pattern: first@domain.com, first.last@domain.com, etc.
        """
        # Call Hunter.io API with free tier
        pass
    
    def verify_email_snov(self, email: str) -> bool:
        """
        Use Snov.io free verification (50 credits/month)
        """
        # Verify email deliverability
        pass
    
    def search_crunchbase(self, industry: str, funding_stage: str = None) -> List[Dict]:
        """
        Crunchbase free tier for funded companies
        Good for: companies with recent funding (they need capital!)
        """
        # API call to Crunchbase free tier
        pass
    
    def enrich_with_clearbit(self, domain: str) -> Dict:
        """
        Clearbit free tier enrichment
        Gets: company size, industry, location, social profiles
        """
        # Clearbit free API call
        pass
    
    def qualify_mca_lead(self, business: Dict) -> Dict:
        """
        Qualify based on MCA criteria:
        - Revenue $15K+/month (estimate from employee count)
        - 6+ months in business
        - 500+ credit score (can't check, but can infer from age)
        """
        score = 0
        qualified = False
        
        # Employee count proxy for revenue
        employees = business.get('employee_count', 0)
        if employees >= 10:
            score += 30
        elif employees >= 5:
            score += 20
        
        # Has website = more established
        if business.get('website'):
            score += 20
        
        # Has phone = contactable
        if business.get('phone'):
            score += 20
        
        # Industry match (trucking, construction, restaurant, motel)
        high_intent_industries = ['trucking', 'construction', 'restaurant', 'motel', 'hotel', 'transportation']
        if any(ind in business.get('industry', '').lower() for ind in high_intent_industries):
            score += 30
        
        if score >= 60:
            qualified = True
        
        return {
            **business,
            'qualification_score': score,
            'qualified': qualified,
            'estimated_monthly_revenue': self._estimate_revenue(employees)
        }
    
    def _estimate_revenue(self, employee_count: int) -> str:
        """Rough revenue estimate based on employee count"""
        if employee_count >= 50:
            return "$500K+"
        elif employee_count >= 20:
            return "$150K-$500K"
        elif employee_count >= 10:
            return "$50K-$150K"
        elif employee_count >= 5:
            return "$25K-$50K"
        else:
            return "Under $25K"
    
    def run_mca_search(self, industry: str, location: str, max_results: int = 50) -> List[Dict]:
        """
        Full pipeline: Search → Enrich → Qualify
        """
        print(f"🔍 Searching for {industry} businesses in {location}...")
        
        # Step 1: Google Places (primary source)
        leads = self.search_google_places(industry, location, max_results)
        self.sources_used.append(f"Google Places: {len(leads)} leads")
        
        # Step 2: Yelp for additional coverage
        yelp_leads = self.scrape_yelp(industry, location, max_results//2)
        self.sources_used.append(f"Yelp: {len(yelp_leads)} leads")
        leads.extend(yelp_leads)
        
        # Step 3: Deduplicate by phone/website
        seen = set()
        unique_leads = []
        for lead in leads:
            key = lead.get('phone') or lead.get('website') or lead.get('name')
            if key and key not in seen:
                seen.add(key)
                unique_leads.append(lead)
        
        # Step 4: Enrich and qualify
        qualified_leads = []
        for lead in unique_leads[:max_results]:
            # Try to enrich with Clearbit if we have website
            if lead.get('website'):
                enrichment = self.enrich_with_clearbit(lead['website'])
                lead.update(enrichment)
            
            # Qualify
            qualified_lead = self.qualify_mca_lead(lead)
            
            if qualified_lead['qualified']:
                qualified_leads.append(qualified_lead)
        
        print(f"✅ Found {len(qualified_leads)} qualified MCA leads")
        print(f"📊 Sources used: {self.sources_used}")
        
        return qualified_leads

if __name__ == "__main__":
    scraper = FreeLeadScraper()
    
    # Example: Find trucking companies in Texas
    leads = scraper.run_mca_search(
        industry="trucking",
        location="Houston, TX",
        max_results=30
    )
    
    # Save results
    with open('/root/.openclaw/workspace/leads_trucking_tx.json', 'w') as f:
        json.dump(leads, f, indent=2)
    
    print(f"\n💾 Saved {len(leads)} leads to leads_trucking_tx.json")
