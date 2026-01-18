#!/usr/bin/env python3
import sqlite3

db_path = r'c:\Users\kumma\Downloads\empower\SPL-2\EmPower\Teacher\Backend\Database\controller.db'

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# These are the EXACT paths we need to replace
REPLACEMENTS = [
    ('Lessons/modules/ক্রিয়া_শিখন(Verb)_মডিউল_1', 'Lessons/modules/Verb_Learning_Module_1'),
    ('Lessons/modules/ক্রিয়া_শিখন(Verb)_মডিউল_2', 'Lessons/modules/Verb_Learning_Module_2'),
    ('Lessons/modules/ক্রিয়া_শিখন(Verb)_মডিউল_3', 'Lessons/modules/Verb_Learning_Module_3'),
    ('Lessons/modules/ক্রিয়া_শিখন(Verb)_মডিউল_4', 'Lessons/modules/Verb_Learning_Module_4'),
    ('Lessons/modules/ক্রিয়া_শিখন(Verb)_মডিউল_5', 'Lessons/modules/Verb_Learning_Module_5'),
]

print("Updating Verb module paths...")
total = 0
for old, new in REPLACEMENTS:
    cursor.execute(
        "UPDATE module_data SET Content_Path = ? WHERE Content_Path = ?",
        (new, old)
    )
    count = cursor.rowcount
    if count > 0:
        print(f"  ✓ {old} -> {new} ({count} rows)")
        total += count
    else:
        print(f"  ✗ {old} (no match)")

conn.commit()
print(f"\nTotal updates: {total}")
conn.close()
