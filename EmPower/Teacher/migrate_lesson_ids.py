#!/usr/bin/env python3
"""
Convert lesson IDs in database from Bengali format to English format.
This script updates the lesson_assigning_data table where Lesson_ID is stored in Bengali format.
"""

import sqlite3
import re

# Database path
DB_PATH = 'Backend/Database/controller.db'

# Mapping of Bengali lesson patterns to English
LESSON_CONVERSIONS = {
    # Pattern format: 'নং_X' -> 'Lesson_X'
    # This will convert any Bengali 'নং_' prefix to 'Lesson_'
}

def convert_lesson_id(lesson_id):
    """
    Convert Bengali lesson ID format to English format.
    Examples:
    - 'নং_7' -> 'Lesson_7'
    - 'নং_6' -> 'Lesson_6'
    """
    if isinstance(lesson_id, str):
        # Replace Bengali 'নং_' with 'Lesson_'
        if 'নং_' in lesson_id:
            return lesson_id.replace('নং_', 'Lesson_')
    return lesson_id


def migrate_lesson_ids():
    """
    Migrate lesson IDs in the lesson_assigning_data table from Bengali to English format.
    """
    try:
        # Connect to the database
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # First, let's see what lesson IDs we have
        print("=" * 60)
        print("LESSON ID MIGRATION - From Bengali to English")
        print("=" * 60)
        
        # Check if table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='lesson_assiging_data'")
        if not cursor.fetchone():
            print("❌ lesson_assiging_data table not found!")
            return False
        
        # Get all unique lesson IDs
        cursor.execute("SELECT DISTINCT Lesson_ID FROM lesson_assiging_data")
        current_ids = cursor.fetchall()
        
        print("\n📊 Current Lesson IDs in database:")
        for (lesson_id,) in current_ids:
            print(f"  - {lesson_id}")
        
        # Convert each lesson ID
        conversions_made = 0
        for (lesson_id,) in current_ids:
            new_lesson_id = convert_lesson_id(lesson_id)
            
            if new_lesson_id != lesson_id:
                print(f"\n🔄 Converting: '{lesson_id}' -> '{new_lesson_id}'")
                
                # Update the database
                cursor.execute(
                    "UPDATE lesson_assiging_data SET Lesson_ID = ? WHERE Lesson_ID = ?",
                    (new_lesson_id, lesson_id)
                )
                conversions_made += 1
                print(f"   ✅ Updated successfully")
        
        # Commit the changes
        conn.commit()
        
        # Show the updated lesson IDs
        cursor.execute("SELECT DISTINCT Lesson_ID FROM lesson_assiging_data")
        updated_ids = cursor.fetchall()
        
        print("\n✅ Updated Lesson IDs in database:")
        for (lesson_id,) in updated_ids:
            print(f"  - {lesson_id}")
        
        print(f"\n📈 Total conversions made: {conversions_made}")
        print("=" * 60)
        print("✅ Migration completed successfully!")
        print("=" * 60)
        
        conn.close()
        return True
        
    except sqlite3.Error as e:
        print(f"❌ Database error: {e}")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


if __name__ == '__main__':
    migrate_lesson_ids()
