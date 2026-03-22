#!/usr/bin/env python3
"""
FREE Email Finder + Outreach Automation
Replaces: Apollo.io ($59/mo) + Make/Zapier ($30/mo) = $89/mo saved
"""

import re
import json
import time
import random
from urllib.parse import urlparse

# Common email patterns
EMAIL_PATTERNS = [
    '{first}@{domain}',
    '{last}@{domain}',
    '{first}.{last}@{domain}',
    '{first}{last}@{domain}',
    '{first}_{last}@{domain}',
    '{first}-{last}@{domain}',
    'info@{domain}',
    'contact@{domain}',
    'hello@{domain}',
    'admin@{domain}',
    'support@{domain}',
    'sales@{domain}',
]

def extract_domain(website):
    """Extract domain from website URL"""
    if not website:
        return None
    
    if not website.startswith('http'):
        website = 'https://' + website
    
    parsed = urlparse(website)
    domain = parsed.netloc.replace('www.', '')
    return domain

def generate_email_variations(first_name, last_name, domain):
    """Generate possible email variations"""
    if not domain:
        return []
    
    emails = []
    first = first_name.lower().strip() if first_name else ''
    last = last_name.lower().strip() if last_name else ''
    
    for pattern in EMAIL_PATTERNS:
        email = pattern.format(first=first, last=last, domain=domain)
        if email not in emails:
            emails.append(email)
    
    return emails

def verify_email_format(email):
    """Basic email format validation"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def find_email_from_website(website, business_name):
    """
    Try to find contact email from website
    This would use Tandem Browser to visit the site
    """
    # Placeholder - would need Tandem integration
    domain = extract_domain(website)
    if domain:
        return [
            f"info@{domain}",
            f"contact@{domain}",
            f"hello@{domain}"
        ]
    return []

def score_lead_quality(lead):
    """
    Score a lead based on available data
    FREE replacement for Apollo.io scoring
    """
    score = 0
    
    # Has phone number (25 pts)
    if lead.get('phone'):
        score += 25
    
    # Has email (20 pts)
    if lead.get('email'):
        score += 20
    
    # Has website (15 pts)
    if lead.get('website'):
        score += 15
    
    # Has physical address (15 pts)
    if lead.get('address'):
        score += 15
    
    # Industry match (15 pts)
    high_value_industries = ['restaurant', 'contractor', 'retail', 'construction', 
                             'plumbing', 'hvac', 'electrician', 'landscaping']
    industry = lead.get('industry', '').lower()
    if any(ind in industry for ind in high_value_industries):
        score += 15
    
    # Recent activity signal (10 pts) - would need social media check
    # For now, check if business name suggests newness
    name = lead.get('business_name', '').lower()
    if any(word in name for word in ['new', 'grand', 'opening', 'now']):
        score += 10
    
    return min(score, 100)

def categorize_lead(score):
    """Categorize lead based on score"""
    if score >= 80:
        return 'hot'
    elif score >= 50:
        return 'warm'
    else:
        return 'cold'

def create_outreach_templates():
    """Create free email templates"""
    templates = {
        'cold_email': """Subject: Quick question about {business_name}

Hi there,

I came across {business_name} and wanted to reach out. I'm Damon, and I help small businesses like yours get fast funding for growth.

Whether it's:
• Purchasing inventory
• Expanding to a new location  
• Covering payroll during busy seasons
• Marketing to bring in more customers

I can help you access $5,000 to $500,000 in as little as 24 hours - no collateral required, just based on your business revenue.

Would you be open to a quick 5-minute call to see if this makes sense for {business_name}?

Best,
Damon Mathewson
MCA Funding Specialist
(Your Phone)

P.S. No credit check required - we fund based on business performance, not personal credit.""",

        'follow_up_1': """Subject: Re: Quick question about {business_name}

Hi again,

Just following up on my email from yesterday about funding options for {business_name}.

I know you're busy running your business, so I'll keep this short:

✓ $5k-$500k available
✓ 24-48 hour funding
✓ No collateral needed
✓ Bad credit OK

Can we schedule a quick call this week? Even 10 minutes could save you thousands.

Best,
Damon""",

        'follow_up_2': """Subject: Last try - {business_name} funding

Hi,

I don't want to be annoying, but I also don't want you to miss out if you need capital for {business_name}.

This will be my last email unless you tell me you're interested.

If you are, reply with "CALL" and I'll call you at a convenient time.

If not, no worries - I'll remove you from my list.

Either way, wishing you success with {business_name}.

Damon""",

        'sms': """Hi, this is Damon. I help businesses like {business_name} get fast funding ($5k-$500k in 24hrs). Interested in a quick call? Reply YES or call me back."""
    }
    
    return templates

def personalize_template(template, lead):
    """Fill in template with lead data"""
    business_name = lead.get('business_name', 'your business')
    
    # Try to extract first name if available
    name = lead.get('contact_name', '')
    if name:
        first_name = name.split()[0]
    else:
        first_name = 'there'
    
    personalized = template.format(
        business_name=business_name,
        first_name=first_name
    )
    
    return personalized

def create_follow_up_sequence(lead):
    """Create a 3-email follow-up sequence"""
    templates = create_outreach_templates()
    
    sequence = [
        {
            'day': 0,
            'type': 'email',
            'subject': f"Quick question about {lead.get('business_name', 'your business')}",
            'body': personalize_template(templates['cold_email'], lead)
        },
        {
            'day': 2,
            'type': 'email',
            'subject': f"Re: Quick question about {lead.get('business_name', 'your business')}",
            'body': personalize_template(templates['follow_up_1'], lead)
        },
        {
            'day': 5,
            'type': 'email',
            'subject': f"Last try - {lead.get('business_name', 'your business')} funding",
            'body': personalize_template(templates['follow_up_2'], lead)
        },
        {
            'day': 7,
            'type': 'sms',
            'body': personalize_template(templates['sms'], lead)
        }
    ]
    
    return sequence

def save_sequence_to_file(lead_id, sequence, output_dir="/root/.openclaw/workspace/leads/sequences"):
    """Save outreach sequence to file"""
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    filename = f"{output_dir}/lead_{lead_id}_sequence.json"
    
    with open(filename, 'w') as f:
        json.dump(sequence, f, indent=2)
    
    print(f"✅ Saved sequence to {filename}")
    return filename

# CLI Interface
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Email Finder + Outreach Automation")
        print("\nUsage:")
        print("  outreach.py templates           - Show email templates")
        print("  outreach.py generate <lead_id> - Generate sequence for lead")
        print("  outreach.py score <json_file>  - Score leads in JSON file")
        sys.exit(0)
    
    cmd = sys.argv[1]
    
    if cmd == "templates":
        templates = create_outreach_templates()
        for name, template in templates.items():
            print(f"\n{'='*60}")
            print(f"TEMPLATE: {name}")
            print('='*60)
            print(template[:500] + "..." if len(template) > 500 else template)
    
    elif cmd == "score" and len(sys.argv) > 2:
        with open(sys.argv[2], 'r') as f:
            leads = json.load(f)
        
        print(f"\nScoring {len(leads)} leads...\n")
        
        hot = warm = cold = 0
        for lead in leads:
            score = score_lead_quality(lead)
            category = categorize_lead(score)
            lead['score'] = score
            lead['category'] = category
            
            if category == 'hot':
                hot += 1
            elif category == 'warm':
                warm += 1
            else:
                cold += 1
        
        # Save scored leads
        output = sys.argv[2].replace('.json', '_scored.json')
        with open(output, 'w') as f:
            json.dump(leads, f, indent=2)
        
        print(f"✅ Scored leads saved to {output}")
        print(f"\nResults:")
        print(f"  🔥 Hot (80+): {hot} leads")
        print(f"  🌡️  Warm (50-79): {warm} leads")
        print(f"  ❄️  Cold (<50): {cold} leads")
    
    else:
        print("Unknown command")
