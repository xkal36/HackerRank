"""
Suppose you have some string SS having length N that is indexed from 0 to N−1. 
You also have some string R that is the reverse of string S. S is funny if the condition 
|S[j] − S[j−1]| = |R[j] − R[j−1| is true for every j from 1 to N−1.

Note: For some string S, S[j] denotes the ASCII value of the jthjth 
zero-indexed character in S. The absolute value of some integer x is written as |x|.

Input Format:

The first line contains an integer, T (the number of test cases). 
The T subsequent lines each contain a string, where the ithith line is string Si.

Constraints:

1 <= T <= 10
0 <= i <= T − 1
2 <= length of Si <= 10000

Output Format:

For each Si, print Funny or Not Funny on a new line.

Sample Input:

2
acxz
bcxz

Sample Output:

Funny
Not Funny
"""


import sys

def get_input():
    inp = sys.stdin.readlines()[1:]
    proper_inp = []
    for i in inp:
        if '\n' in i:
            proper_inp.append(i[:i.find('\n')])
        else:
            proper_inp.append(i)
    return proper_inp
            

def is_funny(s):
    count = 0
    rev_s = ''
    for i in reversed(range(len(s))):
        rev_s += s[i]
    for i in range(len(s) - 1):
        if abs(ord(s[i]) - ord(s[i - 1])) == abs(ord(rev_s[i]) - ord(rev_s[i - 1])):
            count += 1
    if count == len(s) - 1:
        return 'Funny'
    else:
        return 'Not Funny'
    
for inp in get_input():
    print is_funny(inp)