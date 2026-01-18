#!/usr/bin/env python3
import sqlite3

db_path = r'c:\Users\kumma\Downloads\empower\SPL-2\EmPower\Teacher\Backend\Database\controller.db'

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print("Getting current Verb paths...")
cursor.execute("SELECT DISTINCT Content_Path FROM module_data WHERE Content_Type = 2")
paths = cursor.fetchall()

for (path,) in paths:
    print(f"Old: {repr(path)}")
    # Build new path by replacing the Bengali folder name
    new_path = path.replace('ক্রিয়া_শিখন(Verb)_মডিউল', 'Verb_Learning_Module')
    print(f"New: {repr(new_path)}")
    
    if new_path != path:
        cursor.execute(
            "UPDATE module_data SET Content_Path = ? WHERE Content_Path = ?",
            (new_path, path)
        )
        count = cursor.rowcount
        print(f"Updated {count} rows\n")
    else:
        print("No change\n")

conn.commit()
conn.close()

print("\nVerifying...")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute("SELECT Content_Path FROM module_data WHERE Content_Type = 2 ORDER BY Content_ID")
print("Verb paths after update:")
for (path,) in cursor.fetchall():
    print(f"  {path}")
conn.close()
