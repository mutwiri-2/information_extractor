#! python3

# use_phone_numbers.py - a program to find USA phone numbers from text copied to the clipboard and paste back the results to the clipboard.

import pyperclip, re 
# usa phone number regex
phone_number_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?   # area code - optional
    (\s|-|\.)? # separator - optional depending on area code existence
    (\d{3})  # first three digits
    (\s|-|\.) # separator
    (\d{4})  # next four digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension - optional
)''', re.VERBOSE)

# get text from clipboard and 
text = str(pyperclip.paste())

# find matches
matches = []  # list to store strings that match our regexes
# find phone number matches
for groups in phone_number_regex.findall(text):
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phone_num += 'x' + groups[8]
    matches.append(phone_num)

# neatly format the output and copy it to the clipboard ready for use
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print("Copied to clipboard")
    print('\n'.join(matches))
else:
    print("No phone numbers found")
