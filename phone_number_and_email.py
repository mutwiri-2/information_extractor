#! python3

# phone_number_and_email.py - a program to find phone numbers (USA format) and emails from text copied to the clipboard and paste back the results to the clipboard.

import pyperclip, re 
# phone number regex
phone_number_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?   # area code - optional
    (\s|-|\.)? # separator - optional depending on area code existence
    (\d{3})  # first three digits
    (\s|-|\.) # separator
    (\d{4})  # next four digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension - optional
)''', re.VERBOSE)


# email regex
email_regex = re.compile(r"""(
    ([a-zA-Z0-9_%.+-])+  #username
    @  # the at symbol
    ([a-zA-Z0-9-.])  # domain-name
    (\.[a-zA-Z]{2,4})  # top-level domain - dot something .com, .io, .org etc
)""", re.VERBOSE)


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

# find email matches
for groups in email_regex.findall(text):
    matches.append(groups[0])

# TODO - write a phone number regex

# TODO - neatly format the output and copy it to the clipboard ready for use


