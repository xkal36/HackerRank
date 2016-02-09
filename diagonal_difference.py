"""
Given a square matrix of size N × N, calculate the absolute difference between the sums of its diagonals.

Input Format:

The first line contains a single integer, N. The next N lines denote the matrix's rows, 
with each line containing N space-separated integers describing the columns.

Output Format:

Print the absolute difference between the two sums of the matrix's diagonals as a single integer.

Sample Input:

3
11 2 4
4 5 6
10 8 -12

Sample Output:

15
"""


import sys

# Two different approaches:

def diag_diff1(m):
    return abs(sum([m[i][i] for i in range(len(m))]) 
    	- sum([m[::-1][i][i] for i in range(len(m))]))

def diag_diff2(m):
    first_diag_list = [m[i][i] for i in range(len(m))]
    second_diag_list = [m[::-1][i][i] for i in range(len(m))]
    return abs(sum(first_diag_list) - sum(second_diag_list))

def format_input():
    return [map(int, el.split(' ')) for el in sys.stdin.readlines()[1:]]


assert print diag_diff1(format_input()) == print diag_diff2(format_input())

print diag_diff1(format_input())
print diag_diff2(format_input())
