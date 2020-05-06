#! python3

# kenyan_numbers.py - a program to find kenyan numbers from text copied to the clipboard, identify its mobile network operator and then copy the results back to the clipboard

# TODO - define kenyan number regex
import pyperclip, re

kenyan_number_regex = re.compile(r"""(
    (+254|0)   # country code
    (\s|-|,)?   # separator
    (7\d\d)     # prefix
    (\s|-|,)?   # separator
    (\d{6})     # remaining numbers
)""", re.VERBOSE)
