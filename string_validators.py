"""
Task:
You are given a string S. 
Your task is to find out if the string S contains: 
alphanumeric characters, alphabetical characters, 
digits, lowercase and uppercase characters.

Input Format:
A single line containing a string SS.

Constraints:
0 < len(S) <10000 < len(S) <1000

Output Format:
In the first line, print True if S has any alphanumeric characters. Otherwise, print False. 
In the second line, print True if S has any alphabetical characters. Otherwise, print False. 
In the third line, print True if S has any digits. Otherwise, print False. 
In the fourth line, print True if S has any lowercase characters. Otherwise, print False. 
In the fifth line, print True if S has any uppercase characters. Otherwise, print False.

Sample Input:

qA2

Sample Output:

True
True
True
True
True
"""


import sys

def get_input():
    raw_inp = sys.stdin.readlines()
    return [s[:s.find('\n')] if '\n' in s else s for s in raw_inp][0]

def test_string(s):
    tests = ['any_alphanum', 'any_alphab', 'any_digits', 'any_lower', 'any_upper']
    results = {test: False for test in tests}
    for ch in s:
        if ch.isalnum():
            results['any_alphanum'] = True
        if ch.isalpha():
            results['any_alphab'] = True
        if ch.isdigit():
            results['any_digits'] = True
        if ch.islower():
            results['any_lower'] = True
        if ch.isupper():
            results['any_upper'] = True
    for test in tests:
        print results[test]
            
    
test_string(get_input())