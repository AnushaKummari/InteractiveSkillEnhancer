#!/usr/bin/env python3
import sqlite3

db_path = r'c:\Users\kumma\Downloads\empower\SPL-2\EmPower\Teacher\Backend\Database\controller.db'

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Get Type 2 (Verb) entries
cursor.execute("SELECT Content_Path FROM module_data WHERE Content_Type = 2")
print("Verb (Type 2) paths:")
for row in cursor.fetchall():
    path = row[0]
    print(f"  '{path}'")
    # Show the Bengali part in detail
    parts = path.split('/')
    if len(parts) > 2:
        bengali_part = parts[-1]
        print(f"    Bengali part: '{bengali_part}'")
        print(f"    Encoded: {bengali_part.encode('utf-8')}")

conn.close()
