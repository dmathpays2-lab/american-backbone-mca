#!/bin/bash
# FREE MCA Lead Generation Automation Runner
# Replaces: Make/Zapier ($30/mo) + manual work

set -e

echo "=========================================="
echo "MCA LEAD GENERATION SYSTEM - FREE TIER"
echo "=========================================="
echo ""

# Configuration
CITY="${1:-Phoenix AZ}"
INDUSTRY="${2:-restaurants}"
MAX_LEADS="${3:-50}"

echo "🎯 Target: $INDUSTRY in $CITY"
echo "📊 Max Leads: $MAX_LEADS"
echo ""

# Step 1: Scrape Google Maps
echo "Step 1: Scraping Google Maps..."
python3 /root/.openclaw/workspace/scripts/maps_scraper.py "$CITY" "$INDUSTRY" "$MAX_LEADS"

echo ""
echo "Step 2: Processing leads..."

# Get the JSON file that was just created
LEADS_FILE=$(ls -t /root/.openclaw/workspace/leads/${INDUSTRY// /_}_${CITY// /_}*.json 2>/dev/null | head -1)

if [ -z "$LEADS_FILE" ]; then
    echo "❌ No leads file found"
    exit 1
fi

echo "📁 Processing: $LEADS_FILE"

# Step 3: Score leads
echo ""
echo "Step 3: Scoring leads..."
python3 /root/.openclaw/workspace/scripts/outreach.py score "$LEADS_FILE"

# Get the scored file
SCORED_FILE="${LEADS_FILE%.json}_scored.json"

# Step 4: Import to database
echo ""
echo "Step 4: Importing to database..."
python3 /root/.openclaw/workspace/scripts/lead_db.py init
python3 /root/.openclaw/workspace/scripts/lead_db.py add "$SCORED_FILE"

# Step 5: Show stats
echo ""
echo "Step 5: Database stats..."
python3 /root/.openclaw/workspace/scripts/lead_db.py stats

# Step 6: Show hot leads
echo ""
echo "Step 6: Hot leads ready to call..."
python3 /root/.openclaw/workspace/scripts/lead_db.py hot

echo ""
echo "=========================================="
echo "✅ LEAD GENERATION COMPLETE!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Review hot leads above"
echo "2. Call them using your phone"
echo "3. Update status: lead_db.py update <id> contacted"
echo ""
echo "To schedule daily automation, add to crontab:"
echo "0 9 * * * /root/.openclaw/workspace/scripts/run_lead_gen.sh 'Phoenix AZ' restaurants 50"
