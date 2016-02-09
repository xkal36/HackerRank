"""
Given an integer, N, traverse its digits (d1,d2,...,dn) and determine 
how many digits evenly divide N (i.e.: count the number of times N
divided by each digit di has a remainder of 0). Print the number of evenly divisible digits.

Note: Each digit is considered to be unique, so each occurrence of the same evenly divisible 
digit should be counted (i.e.: for N=111, the answer is 3).

Input Format

The first line is an integer, T, indicating the number of test cases. 
The T subsequent lines each contain an integer, N.

Constraints:

1 <= T <= 15
0 < N < 10**9

Output Format:

For every test case, count and print (on a new line) the number of 
digits in N that are able to evenly divide N.

Sample Input:

2
12
1012

Sample Output:

2
3
"""


import sys

def format_input():
    return map(str, map(int, sys.stdin.readlines()[1:]))

def find_digits(n):
    digit_array = [int(i) for i in n]
    count = 0
    for digit in digit_array:
        if digit > 0:
            if int(n) % digit == 0:
                count += 1
    return count

for num in format_input():
    print find_digits(num)