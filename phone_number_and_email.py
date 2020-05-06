#! python3

# phone_number_and_email.py - a program to find phone numbers (USA format) and emails from text copied to the clipboard and paste back the results to the clipboard.

import pyperclip, re 
# phone number regex
phone_number = re.compile(r'''(
    (\d{3}|\(\d{3}\))?   # area code - optional
    (\s|-|\.)? # separator - optional depending on area code existence
    (\d{3})  # first three digits
    (\s|-|\.) # separator
    (\d{4})  # next four digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension - optional
)''', re.VERBOSE)


# TODO - write an email regex

# TODO - get text from clipboard and find matches

# TODO - write a phone number regex

# TODO - neatly format the output and copy it to the clipboard ready for use


