"""
Calvin is driving his favorite vehicle on the 101 freeway. 
He notices that the check engine light of his vehicle is on, 
and he wants to service it immediately to avoid any risks. Luckily, 
a service lane runs parallel to the highway. The length of the service 
lane is N units. The service lane consists of NN segments of equal length and different width.

Calvin can enter to and exit from any segment. Let's call the entry 
segment as index ii and the exit segment as index jj. Assume that the exit 
segment lies after the entry segment (i <= j) and 0 <= i. Calvin has to pass 
through all segments from index i to index j (both inclusive).

Paradise Highway

Calvin has three types of vehicles - bike, car, and truck - 
represented by 11, 22 and 33, respectively. 
These numbers also denote the width of the vehicle.

You are given an array widthwidth of length N, where width[k]width[k] represents 
the width of the kkth segment of the service lane. It is guaranteed that while 
servicing he can pass through at most 10001000 segments, including the entry and exit segments.

If width[k]=1width[k]=1, only the bike can pass through the kkth segment.
If width[k]=2width[k]=2, the bike and the car can pass through the kkth segment.
If width[k]=3width[k]=3, all three vehicles can pass through the kkth segment.
Given the entry and exit point of Calvin's vehicle in the service lane, output 
the type of the largest vehicle which can pass through the service lane (including the entry and exit segments).

Input Format:

The first line of input contains two integers, N and T, where 
N denotes the length of the freeway and T the number of test cases. 
The next line has N space-separated integers which represent the width array.

T test cases follow. Each test case contains two integers, i and j, 
where i is the index of the segment through which Calvin enters the 
service lane and j is the index of the lane segment through which he exits.

Output Format:

For each test case, print the number that represents the largest vehicle type that can pass through the service lane.

Note: Calvin has to pass through all segments from index ii to index jj (both inclusive).

Sample Input:

8 5
2 3 1 2 3 2 3 3
0 3
4 6
6 7
3 5
0 7

Sample Output:

1
2
3
2
1
"""


import sys

def get_smallest(widths, ent_point, ex_point):
    return min(widths[ent_point:ex_point + 1])
 
            
def run_tests():
    raw_inp = sys.stdin.readlines()
    form_inp = [s[:s.find('\n')] if '\n' in s else s for s in raw_inp]
    seg_widths = [int(i) for i in list(form_inp[1]) if i != ' ']
    t_rough = form_inp[2:]
    tests = [(int(i[:i.find(' ')]), int(i[i.find(' '):])) for i in t_rough]
    for test in tests:
        print get_smallest(seg_widths, test[0], test[1])
    
run_tests() 