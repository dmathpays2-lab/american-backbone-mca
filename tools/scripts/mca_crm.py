#!/usr/bin/env python3
"""
Free CRM for MCA Leads
SQLite-based, no monthly fees, fully customizable
"""

import sqlite3
import json
from datetime import datetime
from typing import List, Dict, Optional
from pathlib import Path

class MCACRM:
    """
    Lightweight CRM for MCA lead tracking
    Replaces ActiveCampaign paid plans ($117+/mo)
    """
    
    def __init__(self, db_path: str = "/root/.openclaw/workspace/mca_crm.db"):
        self.db_path = db_path
        self.init_db()
    
    def init_db(self):
        """Create tables if not exist"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Leads table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS leads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                business_name TEXT NOT NULL,
                contact_name TEXT,
                email TEXT,
                phone TEXT,
                website TEXT,
                industry TEXT,
                location TEXT,
                employee_count INTEGER,
                estimated_revenue TEXT,
                qualification_score INTEGER,
                source TEXT,
                status TEXT DEFAULT 'new',  -- new, contacted, qualified, proposal, funded, dead
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                notes TEXT
            )
        ''')
        
        # Activities/interactions table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS activities (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                lead_id INTEGER,
                activity_type TEXT,  -- call, email, meeting, note
                description TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (lead_id) REFERENCES leads (id)
            )
        ''')
        
        # Deals/pipeline table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS deals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                lead_id INTEGER,
                deal_value INTEGER,  -- requested amount
                commission_percent REAL,  -- your commission %
                status TEXT DEFAULT 'prospecting',  -- prospecting, negotiation, underwriting, funded, lost
                probability INTEGER DEFAULT 20,  -- close probability
                expected_close_date TEXT,
                actual_funded_date TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (lead_id) REFERENCES leads (id)
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def add_lead(self, lead_data: Dict) -> int:
        """Add new lead, return lead ID"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO leads (
                business_name, contact_name, email, phone, website,
                industry, location, employee_count, estimated_revenue,
                qualification_score, source, notes
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            lead_data.get('business_name'),
            lead_data.get('contact_name'),
            lead_data.get('email'),
            lead_data.get('phone'),
            lead_data.get('website'),
            lead_data.get('industry'),
            lead_data.get('location'),
            lead_data.get('employee_count'),
            lead_data.get('estimated_revenue'),
            lead_data.get('qualification_score', 0),
            lead_data.get('source', 'manual'),
            lead_data.get('notes', '')
        ))
        
        lead_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return lead_id
    
    def get_leads_by_status(self, status: str) -> List[Dict]:
        """Get all leads with specific status"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM leads WHERE status = ? ORDER BY qualification_score DESC
        ''', (status,))
        
        rows = cursor.fetchall()
        conn.close()
        
        return [dict(row) for row in rows]
    
    def get_pipeline_summary(self) -> Dict:
        """Get pipeline overview for dashboard"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Count by status
        cursor.execute('''
            SELECT status, COUNT(*) as count, 
                   SUM(CASE WHEN qualification_score >= 70 THEN 1 ELSE 0 END) as hot_count
            FROM leads GROUP BY status
        ''')
        lead_summary = {row[0]: {'total': row[1], 'hot': row[2]} for row in cursor.fetchall()}
        
        # Pipeline value
        cursor.execute('''
            SELECT status, SUM(deal_value * commission_percent / 100) as potential_commission
            FROM deals GROUP BY status
        ''')
        pipeline_value = {row[0]: row[1] for row in cursor.fetchall()}
        
        # This month's activity
        cursor.execute('''
            SELECT COUNT(*) FROM activities 
            WHERE created_at >= date('now', 'start of month')
        ''')
        monthly_activities = cursor.fetchone()[0]
        
        conn.close()
        
        return {
            'leads_by_status': lead_summary,
            'pipeline_value': pipeline_value,
            'monthly_activities': monthly_activities,
            'total_leads': sum(s['total'] for s in lead_summary.values()),
            'total_hot_leads': sum(s['hot'] for s in lead_summary.values())
        }
    
    def update_lead_status(self, lead_id: int, new_status: str, note: str = None):
        """Move lead to new status"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE leads SET status = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?
        ''', (new_status, lead_id))
        
        if note:
            cursor.execute('''
                INSERT INTO activities (lead_id, activity_type, description)
                VALUES (?, 'status_change', ?)
            ''', (lead_id, f"Status changed to {new_status}: {note}"))
        
        conn.commit()
        conn.close()
    
    def add_activity(self, lead_id: int, activity_type: str, description: str):
        """Log interaction with lead"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO activities (lead_id, activity_type, description)
            VALUES (?, ?, ?)
        ''', (lead_id, activity_type, description))
        
        conn.commit()
        conn.close()
    
    def create_deal(self, lead_id: int, deal_value: int, commission_percent: float = 3.0):
        """Create new deal from qualified lead"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO deals (lead_id, deal_value, commission_percent, status)
            VALUES (?, ?, ?, 'prospecting')
        ''', (lead_id, deal_value, commission_percent))
        
        # Update lead status
        cursor.execute('''
            UPDATE leads SET status = 'proposal' WHERE id = ?
        ''', (lead_id,))
        
        deal_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return deal_id
    
    def get_daily_tasks(self) -> List[Dict]:
        """Get follow-up tasks for today"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        # Leads that need follow-up (no activity in 3 days, not dead/funded)
        cursor.execute('''
            SELECT l.* FROM leads l
            LEFT JOIN activities a ON l.id = a.lead_id
            WHERE l.status NOT IN ('dead', 'funded')
            GROUP BY l.id
            HAVING MAX(a.created_at) < date('now', '-3 days') OR MAX(a.created_at) IS NULL
            ORDER BY l.qualification_score DESC
            LIMIT 10
        ''')
        
        rows = cursor.fetchall()
        conn.close()
        
        return [dict(row) for row in rows]
    
    def export_to_json(self, filepath: str):
        """Export all leads to JSON for backup/sharing"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM leads')
        leads = [dict(row) for row in cursor.fetchall()]
        
        cursor.execute('SELECT * FROM deals')
        deals = [dict(row) for row in cursor.fetchall()]
        
        conn.close()
        
        export_data = {
            'exported_at': datetime.now().isoformat(),
            'leads': leads,
            'deals': deals
        }
        
        with open(filepath, 'w') as f:
            json.dump(export_data, f, indent=2, default=str)
        
        return filepath

if __name__ == "__main__":
    # Test the CRM
    crm = MCACRM()
    
    # Add sample lead
    lead_id = crm.add_lead({
        'business_name': 'Texas Elite Trucking LLC',
        'contact_name': 'Mike Johnson',
        'phone': '713-555-0123',
        'email': 'mike@texaselitetrucking.com',
        'industry': 'trucking',
        'location': 'Houston, TX',
        'employee_count': 15,
        'estimated_revenue': '$150K-$500K',
        'qualification_score': 85,
        'source': 'google_places'
    })
    
    print(f"✅ Added lead ID: {lead_id}")
    
    # Get pipeline summary
    summary = crm.get_pipeline_summary()
    print(f"\n📊 Pipeline Summary:")
    print(json.dumps(summary, indent=2))
    
    # Export
    crm.export_to_json('/root/.openclaw/workspace/crm_backup.json')
    print(f"\n💾 Exported to crm_backup.json")
