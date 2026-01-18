#!/usr/bin/env python3
import os
import glob

# Test if the media files exist for each module
base_path = r'c:\Users\kumma\Downloads\empower\SPL-2\EmPower\Teacher'

# Check lesson paths
lesson_path = os.path.join(base_path, 'Lessons/Lessons_Chapters/Lesson_1')
media_files = glob.glob(lesson_path + '/media.*')
print(f"Lesson_1 media files: {media_files}")

# Check Noun module
noun_path = os.path.join(base_path, 'Lessons/modules/Noun_Learning_Module_1')
media_files = glob.glob(noun_path + '/media.*')
print(f"Noun_Learning_Module_1 media files: {media_files}")

# Check Verb module
verb_path = os.path.join(base_path, 'Lessons/modules/Verb_Learning_Module_1')
media_files = glob.glob(verb_path + '/media.*')
print(f"Verb_Learning_Module_1 media files: {media_files}")

# Check if folders exist
print(f"\nFolder checks:")
print(f"  Lesson_1 exists: {os.path.exists(lesson_path)}")
print(f"  Noun_Learning_Module_1 exists: {os.path.exists(noun_path)}")
print(f"  Verb_Learning_Module_1 exists: {os.path.exists(verb_path)}")
