"""
Script untuk MEMPERBAIKI semua 8 visualisasi di Metabase
"""

import requests
import json
import time

METABASE_URL = "http://localhost:3000"
METABASE_EMAIL = "root@mail.com"
METABASE_PASSWORD = "root123"
HEADERS = {"Content-Type": "application/json"}

class MetabaseFixVisualizations:
    def __init__(self):
        self.url = METABASE_URL
        self.session = None
        self.database_id = 1
        self.table_id = 9
        
    def login(self):
        print("🔐 Login ke Metabase...")
        response = requests.post(
            f"{self.url}/api/session",
            json={"username": METABASE_EMAIL, "password": METABASE_PASSWORD},
            headers=HEADERS
        )
        
        if response.status_code == 200:
            self.session = response.json()["id"]
            print(f"✅ Login berhasil")
            return True
        else:
            print(f"❌ Login gagal")
            return False
    
    def get_headers(self):
        return {**HEADERS, "X-Metabase-Session": self.session}
    
    def delete_card(self, card_id):
        response = requests.delete(
            f"{self.url}/api/card/{card_id}",
            headers=self.get_headers()
        )
        if response.status_code == 204:
            print(f"  ✅ Card {card_id} dihapus")
            return True
        else:
            print(f"  ⚠️  Card {card_id} tidak ada")
            return False
    
    def create_card(self, card_config):
        response = requests.post(
            f"{self.url}/api/card",
            json=card_config,
            headers=self.get_headers()
        )
        
        if response.status_code == 200:
            card = response.json()
            print(f"  ✅ {card_config['name']} dibuat (ID: {card['id']})")
            return card
        else:
            print(f"  ❌ Gagal: {response.text[:80]}")
            return None
    
    def add_to_dashboard(self, card_id, dashboard_id=2):
        response = requests.post(
            f"{self.url}/api/dashboard/{dashboard_id}/cards",
            json={"cardId": card_id},
            headers=self.get_headers()
        )
        return response.status_code == 200
    
    def fix_all_visualizations(self):
        print("\n" + "="*70)
        print("MEMPERBAIKI SEMUA 8 VISUALISASI")
        print("="*70)
        
        if not self.login():
            return False
        
        visualizations = [
            {
                "id": 52,
                "name": "Total Employees",
                "description": "Total jumlah karyawan",
                "display": "number",
                "query": {
                    "database": self.database_id,
                    "type": "query",
                    "query": {
                        "source-table": self.table_id,
                        "aggregation": [["count"]]
                    }
                }
            },
            {
                "id": 43,
                "name": "Attrition Distribution",
                "description": "Distribusi attrition",
                "display": "bar",
                "query": {
                    "database": self.database_id,
                    "type": "query",
                    "query": {
                        "source-table": self.table_id,
                        "aggregation": [["count"]],
                        "breakout": [["field", 3, {}]]
                    }
                }
            },
            {
                "id": 44,
                "name": "Attrition by Department",
                "description": "Per department",
                "display": "bar",
                "query": {
                    "database": self.database_id,
                    "type": "query",
                    "query": {
                        "source-table": self.table_id,
                        "aggregation": [["count"]],
                        "breakout": [["field", 6, {}]],
                        "filter": ["=", ["field", 3, {}], "Yes"]
                    }
                }
            },
            {
                "id": 45,
                "name": "Attrition by Job Role",
                "description": "Per job role",
                "display": "bar",
                "query": {
                    "database": self.database_id,
                    "type": "query",
                    "query": {
                        "source-table": self.table_id,
                        "aggregation": [["count"]],
                        "breakout": [["field", 16, {}]],
                        "filter": ["=", ["field", 3, {}], "Yes"],
                        "order-by": [["desc", ["aggregation", 0]]]
                    }
                }
            },
            {
                "id": 46,
                "name": "Attrition - Overtime Impact",
                "description": "Per overtime",
                "display": "bar",
                "query": {
                    "database": self.database_id,
                    "type": "query",
                    "query": {
                        "source-table": self.table_id,
                        "aggregation": [["count"]],
                        "breakout": [["field", 23, {}]],
                        "filter": ["=", ["field", 3, {}], "Yes"]
                    }
                }
            },
            {
                "id": 47,
                "name": "Attrition by Job Satisfaction",
                "description": "Per satisfaction",
                "display": "bar",
                "query": {
                    "database": self.database_id,
                    "type": "query",
                    "query": {
                        "source-table": self.table_id,
                        "aggregation": [["count"]],
                        "breakout": [["field", 17, {}]],
                        "filter": ["=", ["field", 3, {}], "Yes"]
                    }
                }
            },
            {
                "id": 48,
                "name": "Attrition by Work-Life Balance",
                "description": "Per WLB",
                "display": "bar",
                "query": {
                    "database": self.database_id,
                    "type": "query",
                    "query": {
                        "source-table": self.table_id,
                        "aggregation": [["count"]],
                        "breakout": [["field", 31, {}]],
                        "filter": ["=", ["field", 3, {}], "Yes"]
                    }
                }
            },
            {
                "id": 49,
                "name": "Attrition by Environment Satisfaction",
                "description": "Per environment",
                "display": "bar",
                "query": {
                    "database": self.database_id,
                    "type": "query",
                    "query": {
                        "source-table": self.table_id,
                        "aggregation": [["count"]],
                        "breakout": [["field", 11, {}]],
                        "filter": ["=", ["field", 3, {}], "Yes"]
                    }
                }
            }
        ]
        
        cards_created = []
        for i, viz in enumerate(visualizations, 1):
            print(f"\n{i}. {viz['name']}")
            
            self.delete_card(viz['id'])
            time.sleep(0.5)
            
            card_config = {
                "name": viz['name'],
                "description": viz['description'],
                "database_id": self.database_id,
                "display": viz['display'],
                "visualization_settings": {},
                "dataset_query": viz['query']
            }
            
            card = self.create_card(card_config)
            if card:
                cards_created.append(card)
                if self.add_to_dashboard(card['id']):
                    print(f"  ✅ Ditambah ke dashboard")
            
            time.sleep(1)
        
        print("\n" + "="*70)
        print(f"✅ SELESAI! {len(cards_created)}/8 visualisasi berhasil")
        print("="*70)
        print(f"\n🔗 Dashboard: {self.url}/dashboard/2")
        print(f"💡 Refresh browser (Ctrl+F5)")
        
        return True

if __name__ == "__main__":
    fixer = MetabaseFixVisualizations()
    fixer.fix_all_visualizations()