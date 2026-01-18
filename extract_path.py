#!/usr/bin/env python3
import sqlite3

db_path = r'c:\Users\kumma\Downloads\empower\SPL-2\EmPower\Teacher\Backend\Database\controller.db'

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("SELECT Content_ID, Content_Path FROM module_data WHERE Content_Type = 2 LIMIT 1")
cid, path = cursor.fetchone()

# Write to a file so we can see the exact content
with open('path_debug.txt', 'w', encoding='utf-8') as f:
    f.write(f"Content_ID: {cid}\n")
    f.write(f"Path repr: {repr(path)}\n")
    f.write(f"Path str: {path}\n")
    f.write(f"Path encoded: {path.encode('utf-8')}\n")
    
    # Check what we're trying to find
    search_str = 'ক্রিয়া_শিখন(Verb)_মডিউল'
    f.write(f"\nSearch string repr: {repr(search_str)}\n")
    f.write(f"Search string in path: {search_str in path}\n")

print("Written to path_debug.txt")
conn.close()
