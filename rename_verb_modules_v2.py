#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

module_path = r'c:\Users\kumma\Downloads\empower\SPL-2\EmPower\Teacher\Lessons\Modules'

# List all folders
print("Current folders in Modules directory:")
for item in os.listdir(module_path):
    item_path = os.path.join(module_path, item)
    if os.path.isdir(item_path):
        print(f"  - {item}")
        # If it contains "Verb", rename it
        if 'Verb' in item or '\u0995\u09cd\u09b0\u09bf' in item:  # ক্রিয়া
            # Extract the number
            parts = item.split('_')
            num = parts[-1]
            new_name = f'Verb_Learning_Module_{num}'
            new_path = os.path.join(module_path, new_name)
            try:
                os.rename(item_path, new_path)
                print(f"    ✓ Renamed to {new_name}")
            except Exception as e:
                print(f"    ✗ Error: {e}")

print("\n✅ Done!")
