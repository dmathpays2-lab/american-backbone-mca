# MCA Lead Generator Source - Codebase Analysis

**Repository:** dmathpays2-lab/mca-lead-generator-source  
**Analysis Date:** 2026-03-21  
**Type:** Vercel Serverless Function API

---

## 1. Top-Level Directory Structure

```
/
├── api/                    # API endpoint handlers
│   └── index.py            # Main application entry point
├── .git/                   # Git version control
├── deployment.tar.gz       # Packaged deployment artifact
├── requirements.txt        # Python dependencies
└── vercel.json             # Vercel deployment configuration
```

### Directory Purposes

| Directory/File | Purpose |
|----------------|---------|
| `api/` | Contains the serverless function handlers for Vercel deployment |
| `deployment.tar.gz` | Compressed archive of the project for deployment |
| `requirements.txt` | Python package dependencies |
| `vercel.json` | Vercel platform configuration (routing, builds) |

---

## 2. Main Entry Points

### Primary Entry Point
- **File:** `api/index.py`
- **Handler Class:** `handler(BaseHTTPRequestHandler)`
- **Deployment Target:** Vercel Serverless Functions

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Root endpoint - returns API status and available endpoints |
| `/api/health` | GET | Health check (handled by root handler) |
| `/api/lead` | POST | Submit lead data |
| `/api/*` | ANY | Catch-all routing to index.py |

---

## 3. Key Modules/Components

### `api/index.py`
The main application file containing a single HTTP request handler class:

#### `handler(BaseHTTPRequestHandler)`
- **Purpose:** Handles all incoming HTTP requests
- **Methods:**
  - `do_GET(self)` - Handles GET requests
    - Returns API status
    - Checks Google Places API key configuration
    - Lists available endpoints
  - `do_POST(self)` - Handles POST requests
    - Accepts lead data submission
    - Returns basic acknowledgment response

#### Environment Variables
- `GOOGLE_PLACES_API_KEY` - API key for Google Places integration

---

## 4. Tech Stack and Dependencies

### Platform
- **Hosting:** Vercel Serverless Functions
- **Runtime:** Python (version managed via `.python-version` in deployment)

### Python Dependencies (`requirements.txt`)
| Package | Version | Purpose |
|---------|---------|---------|
| requests | >=2.31.0 | HTTP library for API calls |

### Standard Library Modules Used
- `http.server.BaseHTTPRequestHandler` - HTTP request handling
- `json` - JSON serialization/deserialization
- `os` - Environment variable access

### Configuration (`vercel.json`)
```json
{
  "version": 2,
  "builds": [{ "src": "api/index.py", "use": "@vercel/python" }],
  "routes": [
    { "src": "/api/(.*)", "dest": "api/index.py" },
    { "src": "/", "dest": "api/index.py" }
  ]
}
```

---

## 5. Architecture Overview

This is a minimal **serverless API** designed for Vercel deployment:

```
Client Request → Vercel Edge → api/index.py (handler class)
                     ↓
              GET /          → Status + Health Check
              POST /api/lead → Lead Submission
```

### Current State
- **Status:** Basic scaffolding/placeholder implementation
- **Functionality:** 
  - Health check endpoint operational
  - Lead submission endpoint accepts data but doesn't process/store it
  - Google Places API integration prepared (key check) but not implemented

### Integration Points
- Google Places API (configured via environment variable)
- Potential lead storage/processing (not yet implemented)

---

## 6. Notes

- This appears to be a **starter template** or **work-in-progress** for an MCA (Merchant Cash Advance) lead generation service
- The actual lead processing logic is not yet implemented
- Deployment is streamlined through Vercel's platform with the `@vercel/python` builder
- The `deployment.tar.gz` file suggests this may be deployed via a CI/CD pipeline or manual deployment process
