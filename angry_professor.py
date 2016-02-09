"""
A Discrete Mathematics professor has a class of N students. 
Frustrated with their lack of discipline, he decides to cancel class if 
fewer than K students are present when class starts.

Given the arrival time of each student, determine if the class is canceled.

Input Format:

The first line of input contains T, the number of test cases.

Each test case consists of two lines. The first line has two space-separated integers, 
N (students in the class) and K (the cancelation threshold). 
The second line contains N space-separated integers (a1,a2,…,aN) 
describing the arrival times for each student.

Note: Non-positive arrival times (ai≤0ai≤0) indicate the student arrived early or on time; 
positive arrival times (ai>0ai>0) indicate the student arrived aiai minutes late.

Output Format:

For each test case, print the word YES if the class is canceled or NO if it is not.

Note: if a student arrives exactly on time (ai=0)(ai=0), the student 
is considered to have entered before the class started.

Sample Input:

2
4 3
-1 -3 4 2
4 2
0 -1 2 1

Sample Output:

YES
NO
"""


import sys

def format_input():
    raw_inp = sys.stdin.readlines()[1:]
    formatted_input = [raw_inp[n:n + 2] for n in range(0, len(raw_inp), 2)]
    return formatted_input
    
    
def class_cancelled(classes):
    outcomes = []
    for ind_class in classes:
        k = int(ind_class[0][ind_class[0].find(' ') + 1: ind_class[0].find('\n')])
        arrival_times = ind_class[1].split(' ')
        num_on_time = sum([1 for i in map(int, arrival_times) if i <= 0])
        if num_on_time >= k:
            outcomes.append('NO')
        else:
            outcomes.append('YES')
    for outcome in outcomes:
        print outcome
    
    
class_cancelled(format_input())