#!/usr/bin/env python3
import sqlite3

db_path = r'c:\Users\kumma\Downloads\empower\SPL-2\EmPower\Teacher\Backend\Database\controller.db'

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Get all Type 2 (Verb) entries
cursor.execute("SELECT Content_ID, Content_Path FROM module_data WHERE Content_Type = 2")
entries = cursor.fetchall()

updates = []
for content_id, old_path in entries:
    # Replace Bengali folder name with English
    new_path = old_path.replace('ক্রিয়া_শিখন(Verb)_মডিউল', 'Verb_Learning_Module')
    if new_path != old_path:
        cursor.execute("UPDATE module_data SET Content_Path = ? WHERE Content_Type = 2 AND Content_ID = ?", (new_path, content_id))
        updates.append((content_id, new_path))

conn.commit()
print(f"Updated {len(updates)} Verb modules")
for cid, path in updates:
    print(f"  ID {cid}: {path}")

conn.close()
