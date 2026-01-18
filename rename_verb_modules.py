#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

module_path = r'c:\Users\kumma\Downloads\empower\SPL-2\EmPower\Teacher\Lessons\Modules'

# Verb Learning modules (ক্রিয়া_শিখন)
for i in range(1, 6):
    old_name = os.path.join(module_path, f'ক্রিয়া_শিখন(Verb)_মডিউল_{i}')
    new_name = os.path.join(module_path, f'Verb_Learning_Module_{i}')
    if os.path.exists(old_name):
        try:
            os.rename(old_name, new_name)
            print(f"✓ Renamed 'ক্রিয়া_শিখন(Verb)_মডিউল_{i}' to 'Verb_Learning_Module_{i}'")
        except Exception as e:
            print(f"✗ Error: {e}")
    else:
        print(f"- Folder not found: {old_name}")

print("\n✅ Done!")
