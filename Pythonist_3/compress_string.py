"""
You are given a string S. Suppose a character 'c' occurs consecutively X times in the string.
Replace these consecutive occurrences of the character 'c' with (X,c) in the string.


Input Format:

A single line of input consisting of the string S.

Output Format:

A single line of output consisting of the modified string.

Constraints:

All the characters of S denote integers between 0 and 9.

1 <= ∣S∣ <= 104

Sample Input:

1222311

Sample Output:

(1, 1) (3, 2) (1, 3) (2, 1)
"""


import itertools

def compress_string(s):
    cons = []
    cons_st = ''
    for x, v in itertools.groupby(list(s)):
        cons.append(list(v))
    for el in cons:
        cons_st += '(%d, %d) ' % (len(el), int(el[0]))
    return cons_st
  
        
print compress_string(raw_input())