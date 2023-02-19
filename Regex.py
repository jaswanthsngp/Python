#Regular Expressions
'''
    Used for pattern matching
    3 types:
        normal
        meta
        special sequences
    meta:
        [].^${}*+?
    special sequnces:
        \d searches for any digit, meta charachters are used for increasing the number of occurences
        \D searches a string without digits
        \w searches word charachters
        \W searches non-word charachters
        \s space (' ')
        \n new line
        \r return
        \0 null
        \ddd Octal 'ddd'
        \b searches a string in the beginning and end of string
    for more info about regex, visit regex101.com
'''
import re
s= 'aaabaa'
regex= 'aa'
print(re.findall(regex, s))         #findall returns list of all the matching occurences
print(re.fullmatch(regex, s))       #returns object if the string completely matches regex
print(re.match(regex, s))           #return object if match is found at first
