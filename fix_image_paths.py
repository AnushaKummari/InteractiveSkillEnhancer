#!/usr/bin/env python3
"""
Fix image paths in generated PyQt5 UI files.
Changes .png references to correct extensions (.jpg for specific files).
Also fixes the cache path bug.
"""

import os
import re

# Mapping of png references that should be jpg
PNG_TO_JPG_REPLACEMENTS = {
    'banner_logo.png': 'banner_logo.jpg',
    'std_lsn.png': 'std_lsn.jpg',
    'assign_records_icon.png': 'assign_records_icon.jpg',
    'std_assessment.png': 'std_assesment.jpg',  # Note: actual file has typo 'assesment'
    'std_perfor.png': 'std_perfor.jpg',
    'banner_icon.png': 'banner_icon.jpg',
    'secondary_banner_logo.png': 'secondary_banner_logo.jpg',
}

# Fix cache path
CACHE_PATH_FIX = (
    r'".\\Frontend\\PyQt_UI\\../../../../../../Cache_Empower/V6/Teacher/Frontend/Images/add_icon.png"',
    r'".\\Frontend\\PyQt_UI\\../Images/add_icon.png"'
)

def fix_ui_files():
    ui_dir = r'c:\Users\kumma\Downloads\empower\SPL-2\EmPower\Teacher\Frontend\Teacher_UI'
    
    if not os.path.exists(ui_dir):
        print(f"Directory not found: {ui_dir}")
        return
    
    files_modified = []
    
    # Process all .py files in the directory
    for filename in os.listdir(ui_dir):
        if filename.startswith('ui_') and filename.endswith('.py'):
            filepath = os.path.join(ui_dir, filename)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            changes_count = 0
            
            # Replace PNG with JPG where needed
            for png_name, jpg_name in PNG_TO_JPG_REPLACEMENTS.items():
                if png_name in content:
                    content = content.replace(png_name, jpg_name)
                    changes_count += len(re.findall(re.escape(png_name), original_content))
                    print(f"  {filename}: {png_name} -> {jpg_name}")
            
            # Fix cache path
            if CACHE_PATH_FIX[0] in content:
                content = content.replace(CACHE_PATH_FIX[0], CACHE_PATH_FIX[1])
                changes_count += 1
                print(f"  {filename}: Fixed cache path")
            
            # Write back if changes were made
            if content != original_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                files_modified.append((filename, changes_count))
                print(f"✓ Modified {filename} ({changes_count} changes)")
    
    print(f"\n{'='*60}")
    print(f"Summary: Modified {len(files_modified)} files")
    for filename, count in files_modified:
        print(f"  - {filename}: {count} fixes")

if __name__ == '__main__':
    print("Fixing image paths in PyQt5 UI files...\n")
    fix_ui_files()
    print("\nDone!")
