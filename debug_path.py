#!/usr/bin/env python3
import sqlite3

db_path = r'c:\Users\kumma\Downloads\empower\SPL-2\EmPower\Teacher\Backend\Database\controller.db'

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Get the exact bytes of a Verb path
cursor.execute("SELECT Content_Path FROM module_data WHERE Content_Type = 2 LIMIT 1")
row = cursor.fetchone()
if row:
    path = row[0]
    print(f"Path: '{path}'")
    print(f"Length: {len(path)}")
    print(f"Repr: {repr(path)}")
    print(f"Bytes: {path.encode('utf-8')}")

conn.close()
