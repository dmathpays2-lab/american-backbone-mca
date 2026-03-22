# MCA SMALL BUSINESS LEAD GENERATION - MASTER STRATEGY
## For: Damon Mathewson | David Allen Capital + Mom and Pop Business Funding

---

## 1. UNDERSTANDING THE MCA MARKET

### What is MCA?
- **Merchant Cash Advance:** Purchase of future revenue at a discount
- **Target:** Small businesses needing $5k-$500k fast (24-48hr funding)
- **Qualifiers:** 3+ months in business, $10k+ monthly revenue
- **No collateral required** - based on bank statements/credit card processing

### Ideal Prospect Profile
| Criteria | Details |
|----------|---------|
| **Business Type** | Restaurants, retail, service businesses, contractors |
| **Revenue** | $10k-$100k/month |
| **Time in Business** | 3+ months (prefer 6+) |
| **Credit** | 500+ FICO (flexible) |
| **Urgency** | Needs capital within 1 week |
| **Use Case** | Expansion, inventory, payroll, equipment, marketing |

---

## 2. LEAD SOURCES - AUTOMATED EXTRACTION

### A. Google Maps Scraping (Primary)
**Target:** Local businesses with "urgency signals"

**Search Queries:**
```
- "restaurants near me" + "newly opened"
- "contractors" + "hiring now"
- "retail stores" + "under new management"
- "small business" + "expanding"
- "food trucks" + "catering"
```

**Data to Extract:**
- Business name
- Phone number
- Address
- Website
- Hours (look for recent changes)
- Reviews (sentiment analysis for growth/urgency)
- Photos (construction/expansion = need capital)

**Automation:**
- Apify Google Maps Scraper
- Schedule daily for new businesses
- Filter by revenue indicators

### B. LinkedIn Sales Navigator
**Target:** Business owners actively posting about growth/challenges

**Filters:**
- Company size: 1-50 employees
- Job title: Owner, Founder, CEO, Manager
- Industry: Retail, Food Service, Construction, Professional Services
- Activity: Posted in last 30 days

**Signals to Watch:**
- "Looking to expand"
- "Hiring"
- "New location"
- "Inventory issues"
- "Equipment needs"

### C. Business Directories (Secondary)
- Yelp (new businesses, high-rated with expansion)
- BBB (complaints = cash flow issues)
- Chamber of Commerce directories
- Industry-specific directories

### D. Social Media Signals
**Instagram/TikTok:**
- Small business hashtags
- "Grand opening" posts
- Behind-the-scenes showing growth
- Equipment purchases

**Twitter/X:**
- Business owner complaints about cash flow
- "Need funding" posts
- Growth announcements

### E. Public Records
- Business license filings (new businesses)
- Commercial real estate leases
- Equipment financing liens
- Lawsuits (cash flow stress indicator)

---

## 3. LEAD QUALIFICATION SYSTEM

### Scoring Matrix (0-100 points)

| Factor | Points | How to Detect |
|--------|--------|---------------|
| **Revenue Indicator** | 0-25 | Website quality, number of locations, employees |
| **Growth Signals** | 0-20 | Hiring posts, expansion, new equipment |
| **Urgency Signals** | 0-20 | Recent cash flow complaints, "need capital" posts |
| **Time in Business** | 0-15 | 3-6mo (10pts), 6-12mo (12pts), 1-2yr (15pts) |
| **Industry Fit** | 0-10 | Restaurants, retail, contractors (high conversion) |
| **Contact Quality** | 0-10 | Direct phone/email vs contact form |

### Hot Leads (80-100 points)
- Multiple growth signals + urgency + direct contact
- **Action:** Call within 1 hour

### Warm Leads (50-79 points)
- Some growth signals, established business
- **Action:** Add to email sequence + call within 24hr

### Cold Leads (0-49 points)
- Limited info, new business, no clear signals
- **Action:** Nurture campaign, check back in 30 days

---

## 4. AUTOMATION WORKFLOWS

### Workflow 1: Google Maps → Qualified Lead (Daily)
```
1. Apify scrapes Google Maps for target industries
2. Extract business details + reviews
3. AI analyzes reviews for growth/urgency signals
4. Score leads using qualification matrix
5. Hot leads → Instant SMS to you
6. Warm leads → Add to CRM + email sequence
7. Cold leads → Database for future nurturing
```

### Workflow 2: LinkedIn → Warm Lead (Daily)
```
1. Sales Navigator filter: Owners/founders in target industries
2. Check recent posts for funding/growth keywords
3. Extract profile + company info
4. Enrich with email finder (Apollo.io, Hunter.io)
5. Score based on post content
6. Add to LinkedIn outreach sequence
```

### Workflow 3: Social Listening → Urgent Leads (Real-time)
```
1. Monitor Twitter/X for keywords: "need funding", "cash flow", "expansion"
2. Filter by business owner profiles
3. Instant alert if high-urgency detected
4. Pull contact info from bio/website
5. Priority queue for immediate outreach
```

### Workflow 4: Email Nurture Sequence
**Day 1:** Introduction + MCA education
**Day 3:** Case study (similar business)
**Day 5:** Funding options comparison
**Day 7:** Direct pitch + calendar link
**Day 10:** Urgency (rates changing soon)
**Day 14:** Final follow-up

---

## 5. TECH STACK FOR AUTOMATION

### Lead Generation
| Tool | Purpose | Cost |
|------|---------|------|
| **Apify** | Google Maps scraping | $49/mo |
| **LinkedIn Sales Navigator** | B2B prospecting | $99/mo |
| **Apollo.io** | Email enrichment | $59/mo |
| **Phantombuster** | Social media extraction | $30/mo |
| **Make.com / Zapier** | Workflow automation | $20-50/mo |

### Lead Management
| Tool | Purpose | Cost |
|------|---------|------|
| **Airtable / Notion** | Lead database | Free-$10/mo |
| **GoHighLevel** | CRM + email/SMS | $97/mo |
| **Calendly** | Booking | Free-$12/mo |

### AI/Analysis
| Tool | Purpose | Cost |
|------|---------|------|
| **OpenAI API** | Review analysis, email drafting | Pay per use |
| **Claude API** | Lead qualification logic | Pay per use |

**Total Monthly Cost:** ~$350-500
**Expected Output:** 50-200 qualified leads/month

---

## 6. IMMEDIATE ACTION PLAN (Week 1)

### Day 1: Setup
- [ ] Set up Apify account
- [ ] Configure Google Maps scraper for 1 target city
- [ ] Test extraction (100 businesses)
- [ ] Set up Airtable/Notion for lead database

### Day 2: Qualification System
- [ ] Build scoring spreadsheet
- [ ] Train AI to analyze reviews/signals
- [ ] Create hot/warm/cold lead categories
- [ ] Set up notification system (SMS/email)

### Day 3: Outreach Templates
- [ ] Write cold call script
- [ ] Draft email sequence (5 emails)
- [ ] Create SMS templates
- [ ] Set up GoHighLevel sequences

### Day 4: LinkedIn Automation
- [ ] Sales Navigator subscription
- [ ] Create search filters
- [ ] Set up connection request sequence
- [ ] Draft LinkedIn messages

### Day 5: Testing
- [ ] Run full workflow end-to-end
- [ ] Call 10 test leads
- [ ] Refine qualification criteria
- [ ] Document results

### Day 6-7: Scale
- [ ] Expand to 5 target cities
- [ ] Add more industries
- [ ] Optimize based on conversion data

---

## 7. SUCCESS METRICS

### Volume Metrics
- **Leads generated:** Daily/weekly count
- **Contact rate:** % of leads reached
- **Conversation rate:** % who engage

### Quality Metrics
- **Application rate:** % who apply for MCA
- **Approval rate:** % approved by funders
- **Funded deals:** $ amount funded

### Efficiency Metrics
- **Cost per lead:** Total cost / leads
- **Cost per funded deal:** Total cost / deals
- **ROI:** Revenue / spend

**Target Benchmarks:**
- 50+ leads/week
- 20% contact rate
- 5% application rate
- 2% funded rate
- $2,000+ commission per funded deal

---

## 8. COMPLIANCE & ETHICS

### Do's ✅
- Only contact businesses publicly listed
- Respect opt-outs immediately
- Be transparent about MCA terms
- Follow TCPA (text) and CAN-SPAM (email) rules
- Document all consent

### Don'ts ❌
- Buy lists (low quality, compliance risk)
- Spam cold contacts
- Misrepresent MCA as "loan"
- Call numbers on DNC list
- Pressure tactics

---

## NEXT STEPS

**Choose your first target:**
1. **Geography:** Which city/region to start?
2. **Industry:** Restaurants? Contractors? Retail?
3. **Budget:** How much for tools/setup?

**Then I'll:**
- Set up the first automation
- Build the lead database
- Create outreach templates
- Start generating leads

**Ready to build your MCA lead machine?** Pick the target market and let's start. ❤️‍🔥
