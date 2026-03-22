# FREE MCA LEAD GENERATION TECH STACK
## Total Monthly Cost: $0 (vs $350-500 paid stack)

---

## PAID vs FREE COMPARISON

| Paid Tool | Cost | FREE Alternative | Status |
|-----------|------|------------------|--------|
| Apify | $49/mo | Python + Tandem Browser | ✅ BUILT |
| LinkedIn Sales Nav | $99/mo | Manual + Tandem scraping | ✅ CAN BUILD |
| Apollo.io | $59/mo | Custom email finder | ✅ BUILT |
| GoHighLevel | $97/mo | SQLite + Python CRM | ✅ BUILT |
| Make/Zapier | $30/mo | Python cron scripts | ✅ BUILT |
| **TOTAL** | **$334/mo** | **$0/mo** | **✅ READY** |

---

## FREE TOOLS BUILT

### 1. Google Maps Scraper (`maps_scraper.py`)
**Replaces:** Apify ($49/mo)
**What it does:**
- Searches Google Maps for businesses by city/industry
- Extracts: name, phone, address, website
- Saves to JSON

**Usage:**
```bash
python3 maps_scraper.py "Phoenix AZ" restaurants 50
```

**Output:** `/root/.openclaw/workspace/leads/restaurants_PhoenixAZ.json`

---

### 2. Lead Database Manager (`lead_db.py`)
**Replaces:** GoHighLevel ($97/mo)
**What it does:**
- SQLite database for lead storage
- Scoring system (0-100)
- Status tracking (new, contacted, qualified, etc.)
- Import/export JSON
- Hot lead listing

**Usage:**
```bash
python3 lead_db.py init              # Setup database
python3 lead_db.py stats             # Show stats
python3 lead_db.py hot               # Show hot leads (70+)
python3 lead_db.py add leads.json    # Import leads
python3 lead_db.py update 1 contacted # Update status
```

**Database:** `/root/.openclaw/workspace/leads/mca_leads.db`

---

### 3. Email Finder + Outreach (`outreach.py`)
**Replaces:** Apollo.io ($59/mo) + Email tools
**What it does:**
- Generates email variations from names/domains
- Lead scoring algorithm
- Email templates (cold, follow-up, SMS)
- Sequence creation

**Usage:**
```bash
python3 outreach.py templates              # Show templates
python3 outreach.py score leads.json       # Score leads
```

**Templates:** Cold email, 2 follow-ups, SMS

---

### 4. Master Automation (`run_lead_gen.sh`)
**Replaces:** Make/Zapier ($30/mo)
**What it does:**
- Runs full pipeline: scrape → score → import → show hot leads
- Can be scheduled with cron

**Usage:**
```bash
./run_lead_gen.sh "Phoenix AZ" restaurants 50
```

**For daily automation:**
```bash
# Add to crontab (runs daily at 9am)
0 9 * * * /root/.openclaw/workspace/scripts/run_lead_gen.sh "Phoenix AZ" restaurants 50
```

---

## WORKFLOW: How It All Works Together

```
┌─────────────────────────────────────────────────────────────┐
│ STEP 1: SCRAPE                                              │
│ Run: ./run_lead_gen.sh "City" "Industry" 50                │
│                                                             │
│ ↓                                                           │
│ Google Maps → Tandem Browser → Business List (JSON)        │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 2: SCORE                                               │
│ Automatic - part of run_lead_gen.sh                        │
│                                                             │
│ ↓                                                           │
│ Analyze: phone, email, website, industry → Score 0-100     │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 3: STORE                                               │
│ Automatic - saves to SQLite database                        │
│                                                             │
│ ↓                                                           │
│ SQLite DB: Categorized as Hot(80+)/Warm(50-79)/Cold(<50)   │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 4: REVIEW HOT LEADS                                    │
│ Run: python3 lead_db.py hot                                │
│                                                             │
│ ↓                                                           │
│ You see: Top 20 leads with highest scores                  │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 5: OUTREACH                                            │
│ Use templates from outreach.py                             │
│                                                             │
│ ↓                                                           │
│ Call/email hot leads, update status in database            │
└─────────────────────────────────────────────────────────────┘
```

---

## ADDITIONAL FREE TOOLS AVAILABLE

### Already Installed:
- **qmd** - Document search/indexing
- **MCP Memory Server** - Fact storage
- **Tandem Browser** - Web automation
- **YouTube API Client** - Video extraction

### Can Build If Needed:
- **LinkedIn Scraper** - Profile extraction via Tandem
- **Social Media Monitor** - Twitter/X keyword tracking
- **Email Sender** - SMTP integration
- **Calendar Integration** - Google Calendar API

---

## WHAT YOU MIGHT NEED TO PAY FOR (Optional)

| Tool | Cost | When Needed |
|------|------|-------------|
| **Google Maps API** | $200 free/mo, then pay | If scraping 10,000+ businesses/mo |
| **Email SMTP** | Free (Gmail) - $10/mo | If sending 100+ emails/day |
| **Phone Number** | $1-5/mo | If you want a business line |
| **Domain** | $12/year | For professional email |

**Estimated REAL cost: $0-20/mo** (vs $350-500 paid stack)

---

## GETTING STARTED

### Step 1: Test the System
```bash
cd /root/.openclaw/workspace/scripts
./run_lead_gen.sh "Phoenix AZ" restaurants 20
```

### Step 2: Review Results
```bash
python3 lead_db.py hot
```

### Step 3: Start Calling
- Use the hot leads list
- Reference the outreach templates
- Update status after each call

### Step 4: Scale
- Add more cities
- Add more industries
- Set up daily automation with cron

---

## FILES LOCATION

```
/root/.openclaw/workspace/
├── scripts/
│   ├── maps_scraper.py      # Google Maps scraper
│   ├── lead_db.py           # Lead database
│   ├── outreach.py          # Email/outreach
│   └── run_lead_gen.sh      # Master automation
├── leads/
│   ├── mca_leads.db         # SQLite database
│   └── *.json               # Scraped leads
└── american-backbone-mca/
    ├── strategy/            # MCA strategy docs
    └── free-tools/          # These tools (backed up)
```

---

## NEXT STEPS

1. **Test it:** Run `./run_lead_gen.sh "Your City" "restaurants" 20`
2. **Refine:** See what data we get, improve extraction
3. **Expand:** Add more industries, more cities
4. **Automate:** Set up cron for daily lead generation

**Ready to test? Pick your first target city and industry.**
