#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import shutil

lessons_path = r'c:\Users\kumma\Downloads\empower\SPL-2\EmPower\Teacher\Lessons'

# Fix the nested structure - move contents from Modules/মডিউলসমূহ to Modules
modules_path = os.path.join(lessons_path, 'Modules')
nested_path = os.path.join(modules_path, 'মডিউলসমূহ')

if os.path.exists(nested_path):
    # Move all contents from nested folder to Modules
    for item in os.listdir(nested_path):
        src = os.path.join(nested_path, item)
        dst = os.path.join(modules_path, item)
        if os.path.exists(dst):
            shutil.rmtree(dst)
        shutil.move(src, dst)
        print(f"✓ Moved '{item}' to Modules/")
    
    # Remove the now-empty nested folder
    os.rmdir(nested_path)
    print(f"✓ Removed empty nested folder")

# Now rename all module subfolders
module_path = os.path.join(lessons_path, 'Modules')

# Noun Learning modules (নাম_শিখন)
for i in range(1, 6):
    old_name = os.path.join(module_path, f'নাম_শিখন(Noun)_মডিউল_{i}')
    new_name = os.path.join(module_path, f'Noun_Learning_Module_{i}')
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"✓ Renamed 'নাম_শিখন(Noun)_মডিউল_{i}' to 'Noun_Learning_Module_{i}'")

# Verb Learning modules (ক্রিয়া_শিখন)
for i in range(1, 6):
    old_name = os.path.join(module_path, f'ক্রিয়া_শিখন(Verb)_মডিউল_{i}')
    new_name = os.path.join(module_path, f'Verb_Learning_Module_{i}')
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"✓ Renamed 'ক্রিয়া_শিখন(Verb)_মডিউল_{i}' to 'Verb_Learning_Module_{i}'")

# Association Learning modules (সম্পর্ক_শিখন)
for i in range(1, 6):
    old_name = os.path.join(module_path, f'সম্পর্ক_শিখন(Association)_মডিউল_{i}')
    new_name = os.path.join(module_path, f'Association_Learning_Module_{i}')
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"✓ Renamed 'সম্পর্ক_শিখন(Association)_মডিউল_{i}' to 'Association_Learning_Module_{i}'")

# Activity Learning module (কর্মধারা_শিখন)
old_name = os.path.join(module_path, 'কর্মধারা_শিখন(Activity)_মডিউল_1')
new_name = os.path.join(module_path, 'Activity_Learning_Module_1')
if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print(f"✓ Renamed 'কর্মধারা_শিখন(Activity)_মডিউল_1' to 'Activity_Learning_Module_1'")

print("\n✅ All folder structure fixed and renames completed!")
