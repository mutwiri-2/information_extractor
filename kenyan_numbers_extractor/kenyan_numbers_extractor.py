#! python3

# kenyan_numbers.py - a program to find kenyan numbers from text copied to the clipboard, identify its mobile network operator and then copy the results back to the clipboard

# define kenyan number regex
import pyperclip, re

kenyan_number_regex = re.compile(r"""(
    (\+254|0)   # country code
    (\s|-)?   # separator
    (7\d{2})     # prefix
    (\s|-)?   # separator
    (\d{6})     # remaining numbers
)""", re.VERBOSE)

# get data from clipboard  
data = str(pyperclip.paste())

# find numbers
numbers = []

for groups in kenyan_number_regex.findall(data):
    # numbers.append(groups[0])
    # phone_num = ' '.join([groups[1], groups[3], groups[5]])
    phone_num = ' '.join(['+254', groups[3], groups[5]])
    numbers.append(phone_num)

# neatly format and output the numbers found
if len(numbers) > 0:
    pyperclip.copy('\n'.join(numbers))
    print('\n'.join(numbers))
    print("Numbers copied to clipboard")
else:
    print("No Kenyan phone numbers found.")
