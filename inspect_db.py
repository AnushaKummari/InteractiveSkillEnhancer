#!/usr/bin/env python3
import sqlite3

db_path = r'c:\Users\kumma\Downloads\empower\SPL-2\EmPower\Teacher\Backend\Database\controller.db'

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Get tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
print("Tables:", [t[0] for t in tables])

# Check lesson_data table
cursor.execute("SELECT * FROM lesson_data LIMIT 2")
print("\nlesson_data columns:", [desc[0] for desc in cursor.description])
for row in cursor.fetchall():
    print("Sample data:")
    for i, desc in enumerate(cursor.description):
        print(f"  {desc[0]}: {row[i]}")

# Check module_data table
cursor.execute("SELECT * FROM module_data LIMIT 2")
print("\nmodule_data columns:", [desc[0] for desc in cursor.description])
for row in cursor.fetchall():
    print("Sample data:")
    for i, desc in enumerate(cursor.description):
        print(f"  {desc[0]}: {row[i]}")

conn.close()
