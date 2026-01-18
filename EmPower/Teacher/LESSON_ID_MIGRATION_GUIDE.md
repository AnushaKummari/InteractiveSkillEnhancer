# Lesson ID Bengali to English Conversion Guide

## Problem
The database currently stores Lesson IDs in Bengali format:
- `নং_1`, `নং_2`, `নং_3`, etc.

These need to be converted to English format:
- `Lesson_1`, `Lesson_2`, `Lesson_3`, etc.

## Solution

### Step 1: Run the Migration Script
This script will convert all existing Lesson IDs in the database from Bengali to English format.

```bash
# Navigate to the Teacher directory
cd EmPower/Teacher

# Run the migration script
python migrate_lesson_ids.py
```

### What the Script Does:
- ✅ Connects to the `controller.db` database
- ✅ Finds all Lesson IDs with Bengali format (`নং_X`)
- ✅ Converts them to English format (`Lesson_X`)
- ✅ Updates the `lesson_assigning_data` table
- ✅ Displays before/after comparison

### Expected Output:
```
============================================================
LESSON ID MIGRATION - From Bengali to English
============================================================

📊 Current Lesson IDs in database:
  - নং_7
  - নং_6
  - নং_3
  - নং_2

🔄 Converting: 'নং_7' -> 'Lesson_7'
   ✅ Updated successfully
🔄 Converting: 'নং_6' -> 'Lesson_6'
   ✅ Updated successfully
...

✅ Updated Lesson IDs in database:
  - Lesson_7
  - Lesson_6
  - Lesson_3
  - Lesson_2

📈 Total conversions made: 4
============================================================
✅ Migration completed successfully!
============================================================
```

### Step 2: Verify the Changes
After running the script, you can verify by:

1. **In the Application**: 
   - Login to the teacher dashboard
   - Go to Lesson Assigning section
   - Check that Lesson IDs now display in English format

2. **Direct Database Check**:
   - Open `Backend/Database/controller.db` with a database browser
   - Check the `lesson_assigning_data` table
   - Confirm all Lesson_ID values use English format

### Step 3: Future Assignments
All new lesson assignments will automatically use English format because the lesson IDs are extracted from the database paths which are already in English.

## File Locations
- **Migration Script**: `EmPower/Teacher/migrate_lesson_ids.py`
- **Database**: `EmPower/Teacher/Backend/Database/controller.db`
- **Lesson Assignment Module**: `EmPower/Teacher/Frontend/src/Lesson_Assigning_Window.py`

## Safety Notes
✅ The script:
- Only modifies the `lesson_assigning_data` table
- Does NOT delete any data
- Creates a backup by converting (not removing original data)
- Can be run multiple times safely (idempotent)
- Provides detailed before/after report

## Rollback
If needed, you can manually revert by reversing the conversion:
- Replace `Lesson_` with `নং_` in the Lesson_ID column

## Questions?
The script handles all Bengali lesson ID formats automatically. Just run it once and you're done!
