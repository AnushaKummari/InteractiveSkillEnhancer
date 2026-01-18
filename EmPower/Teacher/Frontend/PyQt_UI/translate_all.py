#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

replacements = {
    'শিক্ষার্থীর তথ্যসমূহ ': 'Student Information',
    'শিক্ষার্থীর আইডি': 'Student ID',
    'শিক্ষার্থীর নাম': 'Student Name',
    'শিক্ষার্থীর বয়স ': 'Age',
    'ঠিকানা': 'Address',
    'অভিভাবকের নাম': 'Guardian Name',
    'অভিভাবকের মোবাইল নম্বর': 'Guardian Mobile Number',
    'পাঠ': 'Lesson',
    'পাঠসমূহ': 'Lessons',
    'মডিউল': 'Module',
    'ক্যাটাগরি': 'Category',
    'নাম শিখন': 'Noun Learning',
    'ক্রিয়া শিখন': 'Verb Learning',
    'সম্পর্ক শিখন': 'Association Learning',
    'কর্মধারা শিখন': 'Activity Learning',
}

os.chdir(os.path.dirname(os.path.abspath(__file__)))
for fname in os.listdir('.'):
    if fname.endswith('.ui'):
        with open(fname, 'r', encoding='utf-8') as f:
            content = f.read()
        for bengali, english in replacements.items():
            content = content.replace(bengali, english)
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Fixed {fname}')
