#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import shutil

lessons_path = r'c:\Users\kumma\Downloads\empower\SPL-2\EmPower\Teacher\Lessons'

# Rename main folders
old_lessons = os.path.join(lessons_path, 'পাঠসমূহ')
new_lessons = os.path.join(lessons_path, 'Lessons_Chapters')
if os.path.exists(old_lessons):
    os.rename(old_lessons, new_lessons)
    print(f"✓ Renamed 'পাঠসমূহ' to 'Lessons_Chapters'")

old_modules = os.path.join(lessons_path, 'মডিউলসমূহ')
new_modules = os.path.join(lessons_path, 'Modules')
if os.path.exists(old_modules):
    try:
        os.rename(old_modules, new_modules)
        print(f"✓ Renamed 'মডিউলসমূহ' to 'Modules'")
    except PermissionError:
        print(f"⚠ Permission denied renaming 'মডিউলসমূহ'. Trying alternative method...")
        shutil.move(old_modules, new_modules)
        print(f"✓ Renamed 'মডিউলসমূহ' to 'Modules' (using move)")

# Rename lesson subfolders (পাঠ_1 to পাঠ_8)
lessons_chapters_path = new_lessons
for i in range(1, 9):
    old_name = os.path.join(lessons_chapters_path, f'পাঠ_{i}')
    new_name = os.path.join(lessons_chapters_path, f'Lesson_{i}')
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"✓ Renamed 'পাঠ_{i}' to 'Lesson_{i}'")

# Rename module subfolders
modules_path = new_modules

# Noun Learning modules (নাম_শিখন)
for i in range(1, 6):
    old_name = os.path.join(modules_path, f'নাম_শিখন(Noun)_মডিউল_{i}')
    new_name = os.path.join(modules_path, f'Noun_Learning_Module_{i}')
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"✓ Renamed 'নাম_শিখন(Noun)_মডিউল_{i}' to 'Noun_Learning_Module_{i}'")

# Verb Learning modules (ক্রিয়া_শিখন)
for i in range(1, 6):
    old_name = os.path.join(modules_path, f'ক্রিয়া_শিখন(Verb)_মডিউল_{i}')
    new_name = os.path.join(modules_path, f'Verb_Learning_Module_{i}')
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"✓ Renamed 'ক্রিয়া_শিখন(Verb)_মডিউল_{i}' to 'Verb_Learning_Module_{i}'")

# Association Learning modules (সম্পর্ক_শিখন)
for i in range(1, 6):
    old_name = os.path.join(modules_path, f'সম্পর্ক_শিখন(Association)_মডিউল_{i}')
    new_name = os.path.join(modules_path, f'Association_Learning_Module_{i}')
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"✓ Renamed 'সম্পর্ক_শিখন(Association)_মডিউল_{i}' to 'Association_Learning_Module_{i}'")

# Activity Learning module (কর্মধারা_শিখন)
old_name = os.path.join(modules_path, 'কর্মধারা_শিখন(Activity)_মডিউল_1')
new_name = os.path.join(modules_path, 'Activity_Learning_Module_1')
if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print(f"✓ Renamed 'কর্মধারা_শিখন(Activity)_মডিউল_1' to 'Activity_Learning_Module_1'")

print("\n✅ All folder renames completed successfully!")
