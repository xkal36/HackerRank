"""
Shashank likes strings in which consecutive characters are different. 
For example, he likes ABABA, while he doesn't like ABAA. Given a string 
containing characters AA and BB only, he wants to change it into a string he likes. 
To do this, he is allowed to delete the characters in the string.

Your task is to find the minimum number of required deletions.

Input Format:

The first line contains an integer T, i.e. the number of test cases. 
The next T lines contain a string each.

Output Format:

For each test case, print the minimum number of deletions required.

Constraints

1 <= T <= 10
1 <= length of string <= 10**5

Sample Input:

5
AAAA
BBBBB
ABABABAB
BABABA
AAABBB

Sample Output:

3
4
0
0
4
"""


import sys

def format_input():
    raw_inp = sys.stdin.readlines()[1:]
    formatted_inp = [s[:s.find('\n')] if '\n' in s else s for s in raw_inp]
    return formatted_inp

def get_min_deletions_recursive(s, count=0):
    if len(s) == 1:
        return count
    else:
        if s[0] == s[1]:
            count += 1
        return get_min_deletions(s[1:], count)
    
def get_min_deletions(s):
    count = 0
    for i in range(0, len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
    return count
        

for test_case in format_input():
    print get_min_deletions(test_case)