#!/usr/bin/env python3
import sqlite3

db_path = r'c:\Users\kumma\Downloads\empower\SPL-2\EmPower\Teacher\Backend\Database\controller.db'

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print("Fixing Verb module paths...")

# Use LIKE with REPLACE to handle all 5 Verb modules at once
for i in range(1, 6):
    # Using REPLACE function in SQL to swap out the Bengali folder name
    sql = f"""UPDATE module_data 
              SET Content_Path = REPLACE(Content_Path, 'ক্রিয়া_শিখন(Verb)_মডিউল', 'Verb_Learning_Module')
              WHERE Content_Type = 2 AND Content_ID = ?"""
    
    cursor.execute(sql, (i,))
    if cursor.rowcount > 0:
        print(f"  Updated Verb module {i}")

conn.commit()

# Verify
cursor.execute("SELECT Content_ID, Content_Path FROM module_data WHERE Content_Type = 2 ORDER BY Content_ID")
print("\nVerified Verb paths:")
for content_id, path in cursor.fetchall():
    print(f"  Verb_{content_id}: {path}")

conn.close()
