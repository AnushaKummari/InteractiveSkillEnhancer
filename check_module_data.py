#!/usr/bin/env python3
import sqlite3

db_path = r'c:\Users\kumma\Downloads\empower\SPL-2\EmPower\Teacher\Backend\Database\controller.db'

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Check all module_data
cursor.execute("SELECT * FROM module_data")
print("All module_data entries:")
for row in cursor.fetchall():
    print(f"  Type:{row[0]}, ID:{row[1]}, Topic:{row[2]}, Path:{row[3]}")

conn.close()
