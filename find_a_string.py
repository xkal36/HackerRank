"""
In this challenge, the user enters a string and a substring. 
You have to print the number of times that the substring 
occurs in the given string. 
String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Input Format:
The first line of input contains the original string. The next line contains the substring.

Constraints:
1 <= len(string) <= 2001 <= len(string) <= 200 
Each character in the string is an ascii character.

Output Format:
Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input:
ABCDCDC
CDC

Sample Output:
2
"""


import sys

def get_input():
    raw_inp = sys.stdin.readlines()
    form_inp = [s[:s.find('\n')] if '\n' in s else s for s in raw_inp]
    return form_inp

def find_num_occ(s, sub_s):
    return len([n for n in xrange(len(s)) if s.find(sub_s, n) == n])

inp = get_input()
print find_num_occ(inp[0], inp[1])