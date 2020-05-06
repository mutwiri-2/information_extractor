#! python3

# email_extractor.py - a program to find emails from text copied to the clipboard and paste back matches found to the clipboard.

import pyperclip, re 

# email regex
email_regex = re.compile(r"""(
    ([a-zA-Z0-9_%.+-])+  #username
    @  # the at symbol
    ([a-zA-Z0-9-.])  # domain-name
    (\.[a-zA-Z]{2,4})  # top-level domain - dot something .com, .io, .org etc
    (\.[a-zA-Z0-9]{2,4})?  # dot something - optional
)""", re.VERBOSE)


# get text from clipboard and 
text = str(pyperclip.paste())

# find matches
matches = []  # list to store strings that match our regexes

# find email matches
for groups in email_regex.findall(text):
    matches.append(groups[0])

# neatly format the output and copy it to the clipboard ready for use
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print("Copied to clipboard")
    print('\n'.join(matches))
else:
    print("No emails found")


