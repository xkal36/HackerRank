"""
You are given a string S. Your task is to capitalize each word of S.

Input Format:

A single line of input containing the string, S.

Constraints:

0 < len(S) < 1000
The string consists of alphanumeric characters and spaces.

Output Format:

Print the capitalized string, S.

Sample Input:

hello world

Sample Output:

Hello World
"""


import re
import sys

def get_input():
    raw_inp = sys.stdin.readlines()
    return raw_inp

s = get_input()[0]

def repl_func(m):
    return m.group(1) + m.group(2).upper()

s = re.sub("(^|\s)(\S)", repl_func, s)

print re.sub("(^|\s)(\S)", repl_func, s)