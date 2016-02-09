"""
You are given a string SS and width ww. 
Your task is to wrap the string into a paragraph of width ww.

Input Format:

The first line contains a string, SS. 
The second line contains the width, ww.

Constraints:

0 < len(S) < 10000 
0 < w < len(S)

Output Format:

Print the text wrapped paragraph.

Sample Input:

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Sample Output:

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ 
"""


import sys
import textwrap

def get_input():
    raw_inp = sys.stdin.readlines()
    form_inp = [s[:s.find('\r')] if '\r' in s else s for s in raw_inp]
    return form_inp

def wrap_text(inp):
    text = inp[0]
    width = int(inp[1])
    return textwrap.fill(text, width)
    
print wrap_text(get_input())