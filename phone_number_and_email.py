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


# TODO - get text from clipboard and find matches

# TODO - write a phone number regex

# TODO - neatly format the output and copy it to the clipboard ready for use


