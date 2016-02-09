"""
Sid is obsessed with reading short stories. Being a CS student, 
he is doing some interesting frequency analysis with the books. 
He chooses strings S1 and S2 in such a way that |len(S1)−len(S2)| <= 1.

Your task is to help him find the minimum number of characters of the 
first string he needs to change to enable him to make it an anagram of the second string.

Note: A word x is an anagram of another word y if we can produce y by rearranging the letters of x.

Input Format: 
The first line will contain an integer, T, representing the number of test cases. 
Each test case will contain a string having length len(S1) + len(S2), 
which will be concatenation of both the strings described above in the problem.
The given string will contain only characters from a to z.

Output Format: 
An integer corresponding to each test case is printed in a different line, 
i.e. the number of changes required for each test case. Print −1−1 if it is not possible.

Sample Input:

6
aaabbb
ab
abc
mnop
xyyx
xaxbbbxx

Sample Output:

3
1
-1
2
0
1
"""


import sys

def format_input():
    raw_inp = sys.stdin.readlines()[1:]
    formatted_inp = [s[:s.find('\n')] if '\n' in s else s for s in raw_inp]
    return formatted_inp

def get_num_changes(s):
    if len(s) % 2 != 0:
        return -1
    else:
        s1 = s[:len(s) / 2]
        s2 = s[len(s1):]
        num_common = 0
        list_s2 = [ch for ch in s2]
        for letter in s1:
            if letter in list_s2:
                num_common += 1
                list_s2.remove(letter)
    return len(s1) - num_common


for test_case in format_input():
    print get_num_changes(test_case)