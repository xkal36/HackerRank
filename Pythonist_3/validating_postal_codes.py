"""
A postal code P must be a number in the range of (100000−999999). 
A postal code P must not contain more than one alternating repetitive digit pair. 

Alternating repetitive digits are digits which repeat immediately after the next digit. 
In other words, an alternating repetitive digit pair is formed by two equal digits that have just a single digit between them.

For example:

121426 # Here, 1 is an alternating repetitive digit.
523563 # Here, NO digit is an alternating repetitive digit.
552523 # Here, both 2 and 5 are alternating repetitive digits.

Your task is to validate whether PP is a valid postal code or not.

Input Format:

One single line of input containing the string P.

Output Format:

Print "True" if P is valid. Otherwise, print "False". Do not print the quotation marks.

Sample Input:

110000

Sample Output:

False
"""


import sys

def get_input():
    return sys.stdin.readlines()[0]

def val_pos_code(c):
    pairs = [c[i] + c[i + 2] for i in range(len(c) - 2)]
    is_all_digits = [ch.isdigit() for ch in c]
    count_pairs = [(c.count(pair) <= 1) for pair in pairs]
    return (not (False in is_all_digits)) and (100000 <= int(c) <= 999999) and (count_pairs.count(False) <= 1)
    

print val_pos_code(get_input())