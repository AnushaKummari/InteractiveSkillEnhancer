#!/usr/bin/env python3
import sqlite3

db_path = r'c:\Users\kumma\Downloads\empower\SPL-2\EmPower\Teacher\Backend\Database\controller.db'

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Update all remaining paths with মডিউলসমূহ to modules
print("Updating all remaining module paths...")

# First, get all unique paths to see what we have
cursor.execute("SELECT DISTINCT Content_Path FROM module_data WHERE Content_Path LIKE '%মডিউলসমূহ%'")
old_paths = cursor.fetchall()
print(f"Found {len(old_paths)} distinct old paths:")
for path in old_paths:
    print(f"  '{path[0]}'")

# Now update each one
for path in old_paths:
    old_path = path[0]
    # Replace মডিউলসমূহ with modules
    new_path = old_path.replace('মডিউলসমূহ', 'modules')
    
    # For Verb paths: ক্রিয়া_শিখন(Verb)_মডিউল_X -> Verb_Learning_Module_X
    new_path = new_path.replace('ক্রিয়া_শিখন(Verb)_মডিউল_', 'Verb_Learning_Module_')
    
    cursor.execute(
        "UPDATE module_data SET Content_Path = ? WHERE Content_Path = ?",
        (new_path, old_path)
    )
    
    if cursor.rowcount > 0:
        print(f"Updated: '{old_path}' -> '{new_path}' ({cursor.rowcount} rows)")

conn.commit()

# Verify
cursor.execute("SELECT DISTINCT Content_Path FROM module_data WHERE Content_Path LIKE '%মডিউলসমূহ%'")
remaining = cursor.fetchall()
print(f"\nRemaining old paths: {len(remaining)}")

conn.close()
print("Done!")
