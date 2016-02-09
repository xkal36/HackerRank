"""
You are given two strings, AA and BB. Find if there is a substring that appears in both A and B.

Input Format:

Several test cases will be given to you in a single file. 
The first line of the input will contain a single integer T, the number of test cases.

Then there will be T descriptions of the test cases. 
Each description contains two lines. The first line contains the 
string A and the second line contains the string B.

Output Format:

For each test case, display YES (in a newline), if there is a common substring.
Otherwise, display NO.

Constraints:

All the strings contain only lowercase Latin letters.
1 <= T <= 10
1 <= |A|, |B| <= 10**5

Sample Input:

2
hello
world
hi
world

Sample Output:

YES
NO
"""


import sys

def format_input():
    raw_inp = sys.stdin.readlines()[1:]
    formatted_inp = [s[:s.find('\n')] if '\n' in s else s for s in raw_inp]
    return formatted_inp

# First (inefficient) solution:
def exists_substring_slow(s1, s2):
    for letter in s1:
        if letter in s2:
            return 'YES'
    return 'NO'

# Efficient solution:
def exists_substring(s1, s2):
    if set(s1).intersection(set(s2)):
        return 'YES'
    else:
        return 'NO'

new = format_input()
new_len = len(new)
for i in range(0, new_len, 2):
    print exists_substring(new[i], new[i + 1])