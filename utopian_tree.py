"""
The Utopian Tree goes through 2 cycles of growth every year. 
Each spring, it doubles in height. Each summer, its height increases by 1 meter.

Laura plants a Utopian Tree sapling with a height of 1 meter at the onset of spring. 
How tall will her tree be after NN growth cycles?

Input Format:

The first line contains an integer, T, the number of test cases. 
T subsequent lines each contain an integer, N, denoting the number of cycles for that test case.

Constraints:

1 <= T <= 10
0 <= N <= 600

Output Format:

For each test case, print the height of the Utopian Tree after NN cycles. 
Each height must be printed on a new line.

Sample Input:

3
0
1
4

Sample Output:

1
2
7
"""

import sys

def format_input():
    return map(int, sys.stdin.readlines()[1:])


def get_height(num_cycles, height=1):
    for cycle in range(num_cycles):
        if cycle % 2 == 0:
            height *= 2
        else:
            height += 1
    return height

# Recursive version:
def get_height_recursive(num_cycles, height=1, cycle_no=1):
    if num_cycles == 0:
        return height
    else:
        if cycle_no % 2 != 0:
            return get_height(num_cycles - 1, height * 2, cycle_no + 1)
        else:
            return get_height(num_cycles - 1, height + 1, cycle_no + 1)
    

for num in format_input():
    print get_height(num)