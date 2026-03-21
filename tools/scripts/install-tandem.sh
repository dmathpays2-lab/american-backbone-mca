#!/bin/bash
# Tandem Browser Installation Script for OpenClaw
# Created for Damon Mathews - American Backbone

set -e

TANDEM_DIR="$HOME/tandem-browser"
API_TOKEN_FILE="$HOME/.tandem/api-token"

echo "========================================"
echo "TANDEM BROWSER INSTALLER"
echo "For OpenClaw AI Collaboration"
echo "========================================"
echo ""

# Check prerequisites
echo "Checking prerequisites..."

if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found. Please install Node.js 20+ first."
    exit 1
fi

if ! command -v npm &> /dev/null; then
    echo "❌ npm not found. Please install npm first."
    exit 1
fi

NODE_VERSION=$(node --version | cut -d'v' -f2 | cut -d'.' -f1)
if [ "$NODE_VERSION" -lt 20 ]; then
    echo "❌ Node.js version is too old. Need 20+, found $(node --version)"
    exit 1
fi

echo "✅ Node.js $(node --version) detected"
echo "✅ npm $(npm --version) detected"
echo ""

# Clone repository
echo "Step 1: Cloning Tandem Browser repository..."
if [ -d "$TANDEM_DIR" ]; then
    echo "Directory exists. Pulling latest changes..."
    cd "$TANDEM_DIR"
    git pull
else
    git clone https://github.com/hydro13/tandem-browser.git "$TANDEM_DIR"
    cd "$TANDEM_DIR"
fi
echo "✅ Repository ready at $TANDEM_DIR"
echo ""

# Install dependencies
echo "Step 2: Installing dependencies..."
npm install
echo "✅ Dependencies installed"
echo ""

# Create .tandem directory and generate API token
echo "Step 3: Setting up API token..."
mkdir -p "$HOME/.tandem"

if [ -f "$API_TOKEN_FILE" ]; then
    echo "API token already exists. Keeping existing token."
else
    # Generate random token
    API_TOKEN=$(openssl rand -hex 32)
    echo "$API_TOKEN" > "$API_TOKEN_FILE"
    echo "✅ New API token generated"
fi

echo "✅ API token ready at $API_TOKEN_FILE"
echo ""

# Create start script
echo "Step 4: Creating start script..."
cat > "$TANDEM_DIR/start-tandem.sh" << 'EOF'
#!/bin/bash
# Start Tandem Browser with OpenClaw integration

echo "Starting Tandem Browser..."
echo "API will be available at: http://127.0.0.1:8765"
echo ""

# Check if token exists
if [ ! -f "$HOME/.tandem/api-token" ]; then
    echo "❌ API token not found. Run install-tandem.sh first."
    exit 1
fi

# For Linux: use npm start
# For macOS: npm run start:mac (clears quarantine flags)

if [[ "$OSTYPE" == "darwin"* ]]; then
    echo "Detected macOS - clearing quarantine flags..."
    npm run start:mac
else
    echo "Detected Linux - starting normally..."
    npm start
fi
EOF

chmod +x "$TANDEM_DIR/start-tandem.sh"
echo "✅ Start script created: $TANDEM_DIR/start-tandem.sh"
echo ""

# Create verification script
echo "Step 5: Creating verification script..."
cat > "$TANDEM_DIR/verify-tandem.sh" << 'EOF'
#!/bin/bash
# Verify Tandem Browser is running and accessible

echo "Verifying Tandem Browser connection..."
echo ""

API_TOKEN_FILE="$HOME/.tandem/api-token"

if [ ! -f "$API_TOKEN_FILE" ]; then
    echo "❌ API token not found at $API_TOKEN_FILE"
    exit 1
fi

TOKEN=$(cat "$API_TOKEN_FILE")

# Check status
echo "Checking Tandem status..."
STATUS=$(curl -sS http://127.0.0.1:8765/status 2>/dev/null || echo "FAILED")

if [ "$STATUS" = "FAILED" ]; then
    echo "❌ Tandem is not running or not accessible"
    echo "   Make sure to start Tandem first: ./start-tandem.sh"
    exit 1
fi

echo "✅ Tandem is running"
echo "Status: $STATUS"
echo ""

# Check tabs endpoint
echo "Checking tabs API..."
TABS=$(curl -sS http://127.0.0.1:8765/tabs/list \
    -H "Authorization: Bearer $TOKEN" 2>/dev/null || echo "UNAUTHORIZED")

if [ "$TABS" = "UNAUTHORIZED" ]; then
    echo "❌ API token rejected"
    exit 1
fi

echo "✅ API authentication working"
echo "Active tabs: $(echo "$TABS" | grep -c '"id"' || echo "0")"
echo ""

# Check OpenClaw config
if [ -f "$HOME/.openclaw/openclaw.json" ]; then
    echo "✅ OpenClaw config found"
else
    echo "⚠️  OpenClaw config not found at ~/.openclaw/openclaw.json"
    echo "   Wingman chat integration may not work"
fi

echo ""
echo "========================================"
echo "TANDEM IS READY!"
echo "========================================"
echo ""
echo "API Endpoint: http://127.0.0.1:8765"
echo "API Token: $(cat $API_TOKEN_FILE | cut -c1-16)..."
echo ""
echo "Try these commands:"
echo "  curl http://127.0.0.1:8765/status"
echo "  curl http://127.0.0.1:8765/tabs/list -H \"Authorization: Bearer \$(cat ~/.tandem/api-token)\""
EOF

chmod +x "$TANDEM_DIR/verify-tandem.sh"
echo "✅ Verification script created: $TANDEM_DIR/verify-tandem.sh"
echo ""

# Create OpenClaw skill configuration
echo "Step 6: Creating OpenClaw skill configuration..."
mkdir -p "$TANDEM_DIR/skill"
cat > "$TANDEM_DIR/skill/SKILL.md" << 'EOF'
# Tandem Browser Skill for OpenClaw

## Overview
Tandem Browser is a local-first Electron browser built for human-AI collaboration.
It provides a 250+ endpoint local API for OpenClaw to control browsing.

## Connection Details
- API Base URL: `http://127.0.0.1:8765`
- API Token Location: `~/.tandem/api-token`
- Authentication: Bearer token in Authorization header

## Key API Endpoints

### Status & Info
- `GET /status` - Browser status
- `GET /tabs/list` - List all tabs
- `GET /tabs/{id}` - Get tab details

### Navigation
- `POST /tabs/open` - Open new tab
  ```json
  {"url": "https://example.com", "focus": true}
  ```
- `POST /tabs/{id}/navigate` - Navigate tab
- `POST /tabs/{id}/close` - Close tab

### Content Extraction
- `GET /snapshot?compact=true` - Full page snapshot
- `POST /find` - Find elements by text/selector
  ```json
  {"by": "text", "value": "Sign in"}
  ```

### Automation
- `POST /sessions/fetch` - Fetch with session context
- `POST /action/click` - Click element
- `POST /action/type` - Type text

## Usage Example
```python
import requests

# Read token
token = open(os.path.expanduser("~/.tandem/api-token")).read().strip()
headers = {"Authorization": f"Bearer {token}"}

# Open a tab
response = requests.post(
    "http://127.0.0.1:8765/tabs/open",
    headers=headers,
    json={"url": "https://example.com", "focus": false}
)
```

## Security Features
- Six-layer security model between web content and AI
- Domain/IP blocklists
- Outbound POST body scanning for credentials
- AST-level JavaScript analysis
- Behavior monitoring per tab
- Human-in-the-loop for ambiguous/risky actions
EOF

echo "✅ Skill documentation created"
echo ""

# Create helpful commands reference
cat > "$TANDEM_DIR/COMMANDS.md" << 'EOF'
# Tandem Browser Commands Reference

## Quick Start
```bash
# Start Tandem
./start-tandem.sh

# Verify it's working
./verify-tandem.sh

# Check status
curl http://127.0.0.1:8765/status
```

## API Examples

### Get API Token
```bash
TOKEN=$(cat ~/.tandem/api-token)
```

### List Tabs
```bash
curl http://127.0.0.1:8765/tabs/list \
  -H "Authorization: Bearer $TOKEN"
```

### Open New Tab
```bash
curl -X POST http://127.0.0.1:8765/tabs/open \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://youtube.com/watch?v=KQMmAj2IU3o", "focus": true}'
```

### Get Page Snapshot
```bash
curl http://127.0.0.1:8765/snapshot?compact=true \
  -H "Authorization: Bearer $TOKEN"
```

### Find Element by Text
```bash
curl -X POST http://127.0.0.1:8765/find \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"by": "text", "value": "Subscribe"}'
```

### Fetch with Session (for authenticated APIs)
```bash
curl -X POST http://127.0.0.1:8765/sessions/fetch \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "tabId": "tab-1",
    "url": "/api/me",
    "method": "GET"
  }'
```

## Use Cases

### 1. YouTube Video Transcription
Tandem can navigate YouTube and extract content that would normally be blocked
in cloud environments.

### 2. Multi-Tab Research
Open multiple tabs, let OpenClaw summarize each while you browse.

### 3. SPA Inspection
Single-page apps (React/Vue) that are hard to scrape - Tandem renders them fully.

### 4. Authenticated Session Tasks
OpenClaw can operate inside YOUR logged-in sessions (Gmail, banking, etc.)
with your explicit approval.

### 5. Human-in-the-Loop Automation
Captcha solving, 2FA, risky actions - Tandem surfaces these to you instead
of failing silently.
EOF

echo "✅ Commands reference created"
echo ""

# Final summary
echo "========================================"
echo "INSTALLATION COMPLETE!"
echo "========================================"
echo ""
echo "Tandem Browser is installed at: $TANDEM_DIR"
echo ""
echo "NEXT STEPS:"
echo ""
echo "1. Start Tandem Browser:"
echo "   cd $TANDEM_DIR"
echo "   ./start-tandem.sh"
echo ""
echo "2. Verify it's working (in another terminal):"
echo "   cd $TANDEM_DIR"
echo "   ./verify-tandem.sh"
echo ""
echo "3. Start using with OpenClaw:"
echo "   - Tandem will be available at http://127.0.0.1:8765"
echo "   - API token is stored at ~/.tandem/api-token"
echo "   - Wingman panel will appear in browser sidebar"
echo ""
echo "IMPORTANT NOTES:"
echo "- Primary platform: macOS (best support)"
echo "- Secondary: Linux (your system)"
echo "- Windows: Not actively validated"
echo "- This is a developer preview - expect rough edges"
echo ""
echo "For help, see:"
echo "- $TANDEM_DIR/COMMANDS.md"
echo "- $TANDEM_DIR/skill/SKILL.md"
echo "- https://github.com/hydro13/tandem-browser"
echo ""
