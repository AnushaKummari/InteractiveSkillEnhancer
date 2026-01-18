#!/usr/bin/env python3
import sqlite3

db_path = r'c:\Users\kumma\Downloads\empower\SPL-2\EmPower\Teacher\Backend\Database\controller.db'

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Mapping of exact old paths to new paths
REPLACEMENTS = {
    'Lessons/modules/ক্রিয়া_শিখন(Verb)_মডিউল_1': 'Lessons/modules/Verb_Learning_Module_1',
    'Lessons/modules/ক্রিয়া_শিখন(Verb)_মডিউল_2': 'Lessons/modules/Verb_Learning_Module_2',
    'Lessons/modules/ক্রিয়া_শিখন(Verb)_মডিউল_3': 'Lessons/modules/Verb_Learning_Module_3',
    'Lessons/modules/ক্রিয়া_শিখন(Verb)_মডিউল_4': 'Lessons/modules/Verb_Learning_Module_4',
    'Lessons/modules/ক্রিয়া_শিখন(Verb)_মডিউল_5': 'Lessons/modules/Verb_Learning_Module_5',
}

print("Converting Verb module Bengali names to English...")
for old_path, new_path in REPLACEMENTS.items():
    cursor.execute(
        "UPDATE module_data SET Content_Path = ? WHERE Content_Path = ?",
        (new_path, old_path)
    )
    if cursor.rowcount > 0:
        print(f"  {old_path} -> {new_path} ({cursor.rowcount} rows)")

conn.commit()
print(f"Done! Total updates: {sum(1 for _ in REPLACEMENTS)}")
conn.close()
