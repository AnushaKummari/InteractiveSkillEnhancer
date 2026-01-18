#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Comprehensive Bengali to English translation for all .ui files in PyQt_UI folder"""

import os

replacements = {
    # Common UI Elements
    'শিক্ষার্থীর তথ্যসমূহ': 'Student Information',
    'শিক্ষার্থীর আইডি': 'Student ID',
    'শিক্ষার্থীর নাম': 'Student Name',
    'শিক্ষার্থীর বয়স': 'Age',
    'ঠিকানা': 'Address',
    'অভিভাবকের নাম': 'Guardian Name',
    'অভিভাবকের মোবাইল': 'Guardian Mobile',
    'অভিভাবকের মোবাইল নম্বর': 'Guardian Mobile Number',
    'নতুন শিক্ষার্থী যুক্ত করুন': 'Add New Student',
    'শিক্ষার্থীর তথ্য আপডেট করুন': 'Update Student Information',
    'শিক্ষার্থী এন্ট্রি বাতিল করুন': 'Remove Student Entry',
    'তথ্য যুক্ত করুন': 'Add Information',
    
    # Lesson related
    'পাঠ': 'Lesson',
    'পাঠসমূহ': 'Lessons',
    'পাঠে': 'in Lesson',
    'নতুন পাঠ যুক্ত করুন': 'Add New Lesson',
    'পাঠ তৈরি করুন': 'Create Lesson',
    'নতুন লেসন তৈরি করুন': 'Create New Lesson',
    'পাঠ ১': 'Lesson 1',
    'পাঠ ক্রম নির্বাচন করুন': 'Select Lesson Order',
    'পাঠ নির্বাচন করুন': 'Select Lesson',
    'পাঠসূচী': 'Curriculum',
    'পাঠসূচি': 'Curriculum',
    'পাঠ্যসূচী': 'Curriculum',
    'পাঠ মূল্যায়ন': 'Lesson Assessment',
    
    # Module/Category related
    'মডিউল': 'Module',
    'মডিউলের': 'Module',
    'মডিউলের কন্টেন্ট যুক্ত করুন': 'Add Module Content',
    'মডিউল তৈরি করুন': 'Create Module',
    'মডিউলের নাম': 'Module Name',
    'মডিউলটি': 'Module',
    
    # Category options
    'ক্যাটাগরি': 'Category',
    'ক্যাটেগরি': 'Category',
    'ক্যাটাগরি নির্বাচন করুন': 'Select Category',
    'ক্যাটেগরি নির্বাচন করুন': 'Select Category',
    'নাম শিখন (Noun)': 'Noun Learning',
    'নাম শিখন': 'Noun Learning',
    'ক্রিয়া শিখন (Verb)': 'Verb Learning',
    'ক্রিয়া শিখন': 'Verb Learning',
    'সম্পর্ক শিখন (Association)': 'Association Learning',
    'সম্পর্ক শিখন': 'Association Learning',
    'কর্মধারা শিখন (Activity)': 'Activity Learning',
    'কর্মধারা শিখন': 'Activity Learning',
    
    # Task types
    'ধাঁধা': 'Puzzles',
    'ধাঁধার': 'Puzzle',
    'বহুনির্বচনী': 'MCQ',
    'বহুনির্বচনি': 'MCQ',
    'ধারা': 'Sequencing',
    'ধারার': 'Sequencing',
    'শব্দ মিলানো': 'Word Matching',
    'মিলানো': 'Matching',
    
    # Task/Set related
    'সেট': 'Set',
    'সেটের': 'Set',
    'সেটগুলো': 'Sets',
    'সেট নির্বাচন করুন': 'Select Set',
    'প্রশ্ন': 'Question',
    'প্রশ্নের': 'Question',
    'প্রদান': 'Provide',
    'প্রদান করুন': 'Provide',
    'প্রদানের': 'Provide',
    
    # Lesson content
    'পাঠ্যক্রম': 'Lesson Number',
    'পাঠের বিষয়': 'Lesson Topic',
    'পাঠ্যের বিষয়': 'Lesson Topic',
    'বিষয়বস্তু': 'Content',
    'বিবরণ': 'Description',
    'পরিচয়': 'Description',
    'ছবি': 'Image',
    'ছবি/ভিডিও নির্বাচন করুন': 'Select Image/Video',
    'অডিও': 'Audio',
    'অডিও নির্বাচন করুন': 'Select Audio',
    'অডিও রেকর্ড করুন': 'Record Audio',
    'অডিও ফাইলের নাম লিখুন': 'Enter audio file name',
    
    # Buttons
    'সংরক্ষণ করুন': 'Save',
    'সংরক্ষন করুন': 'Save',
    'সংরক্ষ': 'Save',
    'বাতিল': 'Cancel',
    'বাতিল করুন': 'Cancel',
    'ক্লিক': 'Click',
    'যুক্ত করুন': 'Add',
    'আপডেট': 'Update',
    'আপডেট করুন': 'Update',
    'তৈরি': 'Create',
    'তৈরি করুন': 'Create',
    'করুন': 'Submit',
    'করা': 'Done',
    
    # Assignment
    'পাঠ বরাদ্দ করুন': 'Assign Lesson',
    'পাঠ বরাদ্দকরণ উইন্ডো': 'Assign Lesson Window',
    'বরাদ্দ করুন': 'Assign',
    
    # Performance/Reporting
    'শিক্ষার্থীর পারফর্মেন্স': 'Student Performance',
    'পারফর্মেন্স': 'Performance',
    'পারফরম্যান্স': 'Performance',
    'রিপোর্ট': 'Report',
    'গ্রাফ': 'Chart',
    'ডেটা': 'Data',
    'মূল্যায়ন': 'Evaluation',
    
    # Settings
    'সেটিংস': 'Settings',
    
    # Time/UI elements
    'সময়...': 'Time...',
    'সময়': 'Time',
    'যেমনঃ': 'e.g.',
    'যেমন': 'e.g.',
    'অথবা': 'OR',
    'সিলেক্ট': 'Select',
    'সিলেক্ট করুন': 'Select',
    'নির্বাচন': 'Selection',
    'নির্বাচন করুন': 'Select',
}

ui_folder = r'c:\Users\kumma\Downloads\empower\SPL-2\EmPower\Teacher\Frontend\PyQt_UI'
files = [f for f in os.listdir(ui_folder) if f.endswith('.ui')]
print(f"Processing {len(files)} .ui files...")

for fname in files:
    fpath = os.path.join(ui_folder, fname)
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_len = len(content)
        for bn, en in replacements.items():
            content = content.replace(bn, en)
        
        if len(content) != original_len:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Fixed {fname}")
        else:
            print(f"- No changes needed in {fname}")
    except Exception as e:
        print(f"✗ Error in {fname}: {e}")

print("Done!")
