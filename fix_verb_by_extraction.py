#!/usr/bin/env python3
import sqlite3

db_path = r'c:\Users\kumma\Downloads\empower\SPL-2\EmPower\Teacher\Backend\Database\controller.db'

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Get all Verb paths
cursor.execute("SELECT DISTINCT Content_Path FROM module_data WHERE Content_Type = 2")
paths = [p[0] for p in cursor.fetchall()]

print(f"Found {len(paths)} Verb paths to update")

# Get the search pattern from the first path
if paths:
    first_path = paths[0]
    # The format is: Lessons/modules/[BENGALI_FOLDER_NAME]_[NUMBER]
    # We need to find everything before the last underscore and number
    parts = first_path.rsplit('_', 1)  # Split from the right to get number
    folder_with_modules = parts[0]  # This includes "Lessons/modules/ک্রিয়া_শিখন(Verb)_মডিউল"
    number = parts[1]  # This is "1", "2", etc.
    
    # Extract the Bengali part
    bengali_folder = folder_with_modules.replace('Lessons/modules/', '')
    print(f"Bengali folder name: {repr(bengali_folder)}")
    print(f"First path: {first_path}")

# Now update each path
for path in paths:
    # Extract the number from this path
    number = path.rsplit('_', 1)[1]
    new_path = f'Lessons/modules/Verb_Learning_Module_{number}'
    
    print(f"Updating: {new_path}")
    cursor.execute("UPDATE module_data SET Content_Path = ? WHERE Content_Path = ?", (new_path, path))
    print(f"  Rows updated: {cursor.rowcount}")

conn.commit()
conn.close()

print("\nDone!")
