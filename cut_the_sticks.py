"""
You are given NN sticks, where the length of each stick 
is a positive integer. A cut operation is performed on the 
sticks such that all of them are reduced by the length of the smallest stick.

Suppose we have six sticks of the following lengths:
5 4 4 2 2 8

Then, in one cut operation we make a cut of length 2 from 
each of the six sticks. For the next cut operation four sticks are 
left (of non-zero length), whose lengths are the following: 
3 2 2 6

The above step is repeated until no sticks are left.

Given the length of N sticks, print the number of sticks that are left before each subsequent cut operations.

Note: For each cut operation, you have to recalcuate the length of smallest sticks (excluding zero-length sticks).

Input Format 
The first line contains a single integer N. 
The next line contains NN integers: a0, a1,...aN-1 separated by space, where ai represents the length of ith stick.

Output Format 
For each operation, print the number of sticks that are cut, on separate lines.

Constraints 
1 <= N <= 1000 
1 <= ai <= 1000

Sample Input:

6
5 4 4 2 2 8

Sample Output:

6
4
2
1
"""


import sys

def cut_sticks(stick_lengths, cuts=[]):
    if stick_lengths == []:
        return cuts
    else:
        cuts.append(len(stick_lengths))
        return cut_sticks(filter(lambda item: item > 0, 
        	[(i - min(stick_lengths)) for i in stick_lengths]), cuts)

def run_tests():
    raw_inp = [s[:s.find('\n')] if '\n' in s else s for s in sys.stdin.readlines()[1:]]
    formatted_inp = map(int, raw_inp[0].split(' '))
    for i in cut_sticks(formatted_inp):
        print i

run_tests()