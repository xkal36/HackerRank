"""
You are given three integers X, Y and Z representing 
the dimensions of a cuboid. You have to print a list 
of all possible coordinates on a 3D grid where the sum of 
Xi + Yi + Zi is not equal to N. If X = 2, 
the possible values of Xi can be 0, 1 and 2. 
The same applies to Y and Z.

Input Format:
Four integers X, Y, Z and N each on four separate lines, respectively.

Output Format:
Print the list in lexicographic increasing order.

Sample Input:

1
1
1
2

Sample Output:

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
"""


import itertools
import sys

def get_input():
    raw_inp = sys.stdin.readlines()
    form_inp = [s[:s.find('\n')] if '\n' in s else s for s in raw_inp]
    return map(int, form_inp)

def poss_coords(inp):
    n = inp[3]
    all_vals = [range(inp[i] + 1) for i in range(3)]
    return map(list, filter(lambda vals: sum(vals) != n, list(itertools.product(*all_vals))))
    
    
print poss_coords(get_input())
