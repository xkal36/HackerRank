"""
Given a grid of size N × M, each cell in the grid is either good or bad.

A valid plus is defined here as the crossing of two segments (horizontal and vertical) 
of equal lengths. These lengths must be odd, and the middle cell of its horizontal 
segment must cross the middle cell of its vertical segment.

Find the 2 valid pluses that can be drawn on goodgood cells in the grid, and print maximum the product of their areas.

Note: The two pluses cannot overlap, and the product of their areas should be maximum.

Input Format

The first line contains two space-separated integers, N and M.
The N subsequent lines contains M characters, where each character is either G (good) or B (bad). 
If the yth character in the xthxth line is G, then (x,y) is a goodgood cell (otherwise it's a bad cell).

Constraints:

2 <= N <= 15
2 <= M <= 15

Output Format:

Find 2 pluses that can be drawn on goodgood cells of the grid, and print maximum the product of their areas as an integer.

Sample Input 1

5 6
GGGGGG
GBBBGB
GGGGGG
GGBBGB
GGGGGG

Sample Output 1

5

Sample Input 2

6 6
BGBBGB
GGGGGG
BGBBGB
GGGGGG
BGBBGB
BGBBGB

Sample Output 2

25
"""

import re
import sys


def get_input():
    return map(lambda x: x[:x.find('\n')] if '\n' in x else x, sys.stdin.readlines()[1:])
    

def make_grid(lines):
    grid = []
    for row in lines:
        grid.append(list(row))
    return grid

def all_goods(s):
    return re.findall(r'G+', s)
    
def get_goods(grid):
    goods = []
    for row in grid:
        goods.append(all_goods(''.join(row)))
    return goods
   
def column(matrix, i):
    return [row[i] for row in matrix]


def cols(grid):
    cols = []
    for i in range(len(grid[0])):
        cols.append(column(grid, i))
    return cols

def find_pluses(grid):
    rows_good = get_goods(grid)
    cols_good = get_goods(cols(grid))
    return rows_good, cols_good

print find_pluses(get_input())
