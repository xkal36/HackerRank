"""
A group of scientists have broken down species DNA into sequences of integers. 
They determine that two species with the respective DNA sequences A and B are considered to be related 
if a non-decreasing sequence C of the same length can be found, such that Ci = Ai or Ci = Bi.

Given the DNA sequences for two species, help the scientists determine if they are related.

Input Format:

The first line contains an integer, T, the number of test cases.

For each test case: 
The first line contains an integer, N, the length of the DNA sequence. 
The second line contains a sequence of space-separated integers describing species A. 
The third line contains a sequence of space-separated integers describing species B.

Constraints: 
1 <= T <= 5
1 <= N <= 10**5
0 <= Ai, Bi <= 10**10

Output Format:

On a new line for each test case, print YES if a non-decreasing sequence of the same 
length can be found (i.e.: species are related) or NO if it cannot.

Sample Input:

3
3
1 2 3
4 4 4
3
3 2 1
6 5 4
2
1 0
10 2

Sample Output:

YES
NO
YES
"""


import itertools
import sys
 
def non_decreasing(l1, l2):
    tups = zip(l1, l2)
    current = min(tups[0])
    for i in range(1, len(l1)):
        if tups[i][0] >= current and tups[i][1] >= current:
            current = min(tups[i][0], tups[i][1])
        elif tups[i][0] >= current:
            current = tups[i][0]
        elif tups[i][1] >= current:
            current = tups[i][1]
        else:
            return 'NO'
    return 'YES'


for i in range(int(raw_input())):
    seq_len = raw_input()
    A = map(long, str(raw_input()).split(' '))
    B = map(long, str(raw_input()).split(' '))
    print non_decreasing(A, B)