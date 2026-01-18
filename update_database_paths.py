#!/usr/bin/env python3
"""
Update all Bengali folder paths in controller.db to English names.
"""

import sqlite3
import os

# Mapping of Bengali paths to English paths
LESSON_RENAMES = {
    'পাঠসমূহ/পাঠ_1': 'Lessons_Chapters/Lesson_1',
    'পাঠসমূহ/পাঠ_2': 'Lessons_Chapters/Lesson_2',
    'পাঠসমূহ/পাঠ_3': 'Lessons_Chapters/Lesson_3',
    'পাঠসমূহ/পাঠ_4': 'Lessons_Chapters/Lesson_4',
    'পাঠসমূহ/পাঠ_5': 'Lessons_Chapters/Lesson_5',
    'পাঠসমূহ/পাঠ_6': 'Lessons_Chapters/Lesson_6',
    'পাঠসমূহ/পাঠ_7': 'Lessons_Chapters/Lesson_7',
    'পাঠসমূহ/পাঠ_8': 'Lessons_Chapters/Lesson_8',
}

MODULE_RENAMES = {
    'নাম_শিখন(Noun)_মডিউল_1': 'Noun_Learning_Module_1',
    'নাম_শিখন(Noun)_মডিউল_2': 'Noun_Learning_Module_2',
    'নাম_শিখন(Noun)_মডিউল_3': 'Noun_Learning_Module_3',
    'নাম_শিখন(Noun)_মডিউল_4': 'Noun_Learning_Module_4',
    'নাম_শিখন(Noun)_মডিউল_5': 'Noun_Learning_Module_5',
    
    'ক্রিয়া_শিখন(Verb)_মডিউল_1': 'Verb_Learning_Module_1',
    'ক্রিয়া_শিখন(Verb)_মডিউল_2': 'Verb_Learning_Module_2',
    'ক্রিয়া_শিখন(Verb)_মডিউল_3': 'Verb_Learning_Module_3',
    'ক্রিয়া_শিখন(Verb)_মডিউল_4': 'Verb_Learning_Module_4',
    'ক্রিয়া_শিখন(Verb)_মডিউল_5': 'Verb_Learning_Module_5',
    
    'সম্পর্ক_শিখন(Association)_মডিউল_1': 'Association_Learning_Module_1',
    'সম্পর্ক_শিখন(Association)_মডিউল_2': 'Association_Learning_Module_2',
    'সম্পর্ক_শিখন(Association)_মডিউল_3': 'Association_Learning_Module_3',
    'সম্পর্ক_শিখন(Association)_মডিউল_4': 'Association_Learning_Module_4',
    'সম্পর্ক_শিখন(Association)_মডিউল_5': 'Association_Learning_Module_5',
    
    'কার্যকলাপ_শিখন_মডিউল_1': 'Activity_Learning_Module_1',
    'কর্মধারা_শিখন(Activity)_মডিউল_1': 'Activity_Learning_Module_1',
}

def update_database():
    db_path = r'c:\Users\kumma\Downloads\empower\SPL-2\EmPower\Teacher\Backend\Database\controller.db'
    
    if not os.path.exists(db_path):
        print(f"Database not found: {db_path}")
        return
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        total_updates = 0
        
        # Update lesson_data table
        print("Updating lesson_data table...")
        for old_path, new_path in LESSON_RENAMES.items():
            old_full = f'Lessons/{old_path}'
            new_full = f'Lessons/{new_path}'
            cursor.execute(
                "UPDATE lesson_data SET Lesson_Path = ? WHERE Lesson_Path = ?",
                (new_full, old_full)
            )
            if cursor.rowcount > 0:
                print(f"  {old_full} → {new_full} ({cursor.rowcount} rows)")
                total_updates += cursor.rowcount
        
        # Update module_data table
        print("\nUpdating module_data table...")
        for old_path, new_path in MODULE_RENAMES.items():
            old_full = f'Lessons/মডিউলসমূহ/{old_path}'
            new_full = f'Lessons/modules/{new_path}'
            cursor.execute(
                "UPDATE module_data SET Content_Path = ? WHERE Content_Path = ?",
                (new_full, old_full)
            )
            if cursor.rowcount > 0:
                print(f"  {old_full} → {new_full} ({cursor.rowcount} rows)")
                total_updates += cursor.rowcount
        
        conn.commit()
        print(f"\n{'='*60}")
        print(f"Total updates: {total_updates}")
        conn.close()
        print("✓ Database updated successfully!")
        
    except Exception as e:
        print(f"✗ Error updating database: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    print("Updating database paths from Bengali to English...\n")
    update_database()
    print("\nDone!")
