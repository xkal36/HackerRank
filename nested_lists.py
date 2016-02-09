"""
Given the names and grades for each student 
in a Physics class of N students, 
store them in a nested list and print the name(s) 
of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, 
order their names alphabetically and print each name on a new line.

Input Format:
The first line contains an integer, N, the number of students. 
The 2N subsequent lines describe each student over 2 lines; 
the first line contains a student's name, and the second line contains their grade.

Constraints:
2 <= N <= 52 <= N <= 5
There will always be one or more students having the second lowest grade.

Output Format:
Print the name(s) of any student(s) having the second 
lowest grade in Physics; if there are multiple students, 
order their names alphabetically and print each one on a new line.

Sample Input:

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output:

Berry
Harry
"""


import sys

def get_input():
    raw_inp = sys.stdin.readlines()[1:]
    inp = [s[:s.find('\n')] if '\n' in s else s for s in raw_inp]
    form_inp = [inp[i: i + 2] for i in range(0, len(inp), 2)]
    return [[inp[0], float(inp[1])] for inp in form_inp]

def get_snd_smallest(l):
    smallest = min(l)
    return min([el for el in l if el > smallest])


def get_snd_lowest_stu(records):
    snd_lowest = get_snd_smallest([record[1] for record in records])
    snd_lowest_stus = [record[0] for record in records if record[1] == snd_lowest]
    for stu in sorted(snd_lowest_stus):
        print stu

get_snd_lowest_stu(get_input())