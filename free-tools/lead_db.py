#!/usr/bin/env python3
"""
FREE Lead Database Manager
Uses SQLite (no GoHighLevel needed) - $97/mo saved
"""

import sqlite3
import json
import os
from datetime import datetime

DB_PATH = "/root/.openclaw/workspace/leads/mca_leads.db"

def init_db():
    """Initialize the lead database"""
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            business_name TEXT NOT NULL,
            phone TEXT,
            email TEXT,
            address TEXT,
            city TEXT,
            state TEXT,
            website TEXT,
            industry TEXT,
            source TEXT,
            score INTEGER DEFAULT 0,
            status TEXT DEFAULT 'new',
            notes TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            contacted_at TIMESTAMP,
            contacted_count INTEGER DEFAULT 0
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS interactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lead_id INTEGER,
            type TEXT, -- 'call', 'email', 'sms'
            outcome TEXT, -- 'no_answer', 'interested', 'not_interested', 'callback'
            notes TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (lead_id) REFERENCES leads (id)
        )
    ''')
    
    conn.commit()
    conn.close()
    print("✅ Lead database initialized")

def add_lead(business_name, phone=None, email=None, address=None, 
             city=None, state=None, website=None, industry=None, 
             source=None, score=0, notes=None):
    """Add a new lead to the database"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO leads (business_name, phone, email, address, city, state, 
                          website, industry, source, score, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (business_name, phone, email, address, city, state, 
          website, industry, source, score, notes))
    
    conn.commit()
    lead_id = cursor.lastrowid
    conn.close()
    
    return lead_id

def get_leads_by_score(min_score=0, status='new', limit=50):
    """Get leads filtered by score and status"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT * FROM leads 
        WHERE score >= ? AND status = ?
        ORDER BY score DESC, created_at DESC
        LIMIT ?
    ''', (min_score, status, limit))
    
    leads = cursor.fetchall()
    conn.close()
    
    return leads

def update_lead_status(lead_id, status):
    """Update lead status (new, contacted, qualified, not_interested, funded)"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        UPDATE leads SET status = ?, contacted_at = CURRENT_TIMESTAMP, 
                        contacted_count = contacted_count + 1
        WHERE id = ?
    ''', (status, lead_id))
    
    conn.commit()
    conn.close()

def add_interaction(lead_id, type_, outcome, notes=None):
    """Log an interaction with a lead"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO interactions (lead_id, type, outcome, notes)
        VALUES (?, ?, ?, ?)
    ''', (lead_id, type_, outcome, notes))
    
    conn.commit()
    conn.close()

def get_lead_stats():
    """Get database statistics"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('SELECT COUNT(*) FROM leads')
    total_leads = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM leads WHERE status = 'new'")
    new_leads = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM leads WHERE status = 'contacted'")
    contacted = cursor.fetchone()[0]
    
    cursor.execute('SELECT AVG(score) FROM leads')
    avg_score = cursor.fetchone()[0] or 0
    
    conn.close()
    
    return {
        'total_leads': total_leads,
        'new_leads': new_leads,
        'contacted': contacted,
        'avg_score': round(avg_score, 1)
    }

def export_leads_to_json(filename=None):
    """Export all leads to JSON for backup"""
    if filename is None:
        filename = f"/root/.openclaw/workspace/leads/backup_{datetime.now().strftime('%Y%m%d')}.json"
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM leads')
    leads = cursor.fetchall()
    
    # Get column names
    cursor.execute('PRAGMA table_info(leads)')
    columns = [col[1] for col in cursor.fetchall()]
    
    conn.close()
    
    # Convert to dict
    leads_dict = []
    for lead in leads:
        leads_dict.append(dict(zip(columns, lead)))
    
    with open(filename, 'w') as f:
        json.dump(leads_dict, f, indent=2, default=str)
    
    print(f"✅ Exported {len(leads)} leads to {filename}")
    return filename

def import_leads_from_json(json_file, source="import"):
    """Import leads from JSON file"""
    with open(json_file, 'r') as f:
        leads = json.load(f)
    
    count = 0
    for lead in leads:
        add_lead(
            business_name=lead.get('business_name', 'Unknown'),
            phone=lead.get('phone'),
            email=lead.get('email'),
            address=lead.get('address'),
            city=lead.get('city'),
            state=lead.get('state'),
            website=lead.get('website'),
            industry=lead.get('industry'),
            source=source,
            score=lead.get('score', 0),
            notes=lead.get('notes')
        )
        count += 1
    
    print(f"✅ Imported {count} leads from {json_file}")
    return count

def list_hot_leads(limit=20):
    """Show hot leads (score 70+)"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT id, business_name, phone, score, industry, city
        FROM leads
        WHERE score >= 70 AND status = 'new'
        ORDER BY score DESC
        LIMIT ?
    ''', (limit,))
    
    leads = cursor.fetchall()
    conn.close()
    
    if not leads:
        print("No hot leads found.")
        return
    
    print(f"\n🔥 HOT LEADS (Score 70+):\n")
    print(f"{'ID':<5} {'Business':<30} {'Phone':<15} {'Score':<6} {'Industry':<15} {'City':<15}")
    print("-" * 90)
    
    for lead in leads:
        print(f"{lead[0]:<5} {lead[1]:<30} {lead[2] or 'N/A':<15} {lead[3]:<6} {lead[4] or 'N/A':<15} {lead[5] or 'N/A':<15}")

# CLI Interface
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Lead Database Manager")
        print("\nUsage:")
        print("  lead_db.py init                    - Initialize database")
        print("  lead_db.py stats                   - Show statistics")
        print("  lead_db.py hot                     - Show hot leads")
        print("  lead_db.py add <json_file>         - Add leads from JSON")
        print("  lead_db.py export                  - Export to JSON")
        print("  lead_db.py update <id> <status>   - Update lead status")
        sys.exit(0)
    
    cmd = sys.argv[1]
    
    if cmd == "init":
        init_db()
    elif cmd == "stats":
        stats = get_lead_stats()
        print(f"\n📊 LEAD DATABASE STATS:")
        print(f"Total Leads: {stats['total_leads']}")
        print(f"New Leads: {stats['new_leads']}")
        print(f"Contacted: {stats['contacted']}")
        print(f"Avg Score: {stats['avg_score']}")
    elif cmd == "hot":
        init_db()
        list_hot_leads()
    elif cmd == "add" and len(sys.argv) > 2:
        init_db()
        import_leads_from_json(sys.argv[2])
    elif cmd == "export":
        export_leads_to_json()
    elif cmd == "update" and len(sys.argv) > 3:
        update_lead_status(int(sys.argv[2]), sys.argv[3])
        print(f"✅ Updated lead {sys.argv[2]} to status: {sys.argv[3]}")
    else:
        print("Unknown command")
