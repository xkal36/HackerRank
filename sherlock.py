"""
Sherlock Holmes suspects his archenemy, Professor Moriarty, is once again plotting 
something diabolical. Sherlock's companion, Dr. Watson, suggests Moriarty 
may be responsible for MI6's recent issues with their supercomputer, The Beast.

Shortly after resolving to investigate, Sherlock receives a note from Moriarty 
boasting about infecting The Beast with a virus; however, he also gives him a clue—a number, N. 
Sherlock determines the key to removing the virus is to find the largest 
Decent Number having N digits.

A Decent Number has the following properties:

Its digits can only be 3's and/or 5's.
The number of 3's it contains is divisible by 5.
The number of 5's it contains is divisible by 3.
If there are more than one such number, we pick the largest one.
Moriarty's virus shows a clock counting down to The Beast's destruction, 
and time is running out fast. Your task is to help Sherlock find the key 
before The Beast is destroyed!

Constraints:

1 <= T <= 20
1 <= N <= 100000


Input Format:

The first line is an integer, T, denoting the number of test cases.

The T subsequent lines each contain an integer, N, detailing the number of digits in the number.

Output Format:

Print the largest Decent Number having NN digits; if no such number exists, 
tell Sherlock by printing -1.
"""


import sys

def format_input():
    return map(int, sys.stdin.readlines()[1:])


def get_largest_dec(n):
    c = 5*(2*n%3)
    if c > n:
        print -1
    else:
        print ('5' * (n-c) + '3'*c)
            
for num in format_input():
    get_largest_dec(num)