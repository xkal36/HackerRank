"""
James found a love letter his friend Harry has written for his girlfriend. 
James is a prankster, so he decides to meddle with the letter. 
He changes all the words in the letter into palindromes.

To do this, he follows two rules:

He can reduce the value of a letter, e.g. he can change d to c, but he cannot change c to d.
In order to form a palindrome, if he has to repeatedly reduce the value of a letter, he can do 
it until the letter becomes a. Once a letter has been changed to a, it can no longer be changed.
Each reduction in the value of any letter is counted as a single operation. 
Find the minimum number of operations required to convert a given string into a palindrome.

Input Format:

The first line contains an integer T, i.e., the number of test cases. 
The next T lines will contain a string each. The strings do not contain any spaces.

Constraints:
1 <= T <= 10
1 ≤ length of string <= 10**4
All characters are lower case English letters.

Output Format:

A single line containing the number of minimum operations corresponding to each test case.

Sample Input:

4
abc
abcba
abcd
cba

Sample Output:

2
0
4
2
"""


import string
import sys

def get_num_ops(s):
    if s == s[::-1]:
        return 0
    else:
        list_s = list(s)
        alph = string.lowercase
        len_s = len(s) 
        index = 0
        num_ops = 0
        while index < len_s:
            if s[index] != s[(len_s - 1) - index]:
                if s[(len_s - 1) - index] > s[index]:
                    list_s[(len_s - 1) - index] = list_s[index]
                else:
                    list_s[index] = list_s[(len_s - 1) - index]
                num_ops += abs(alph.find(s[(len_s - 1) - index]) - alph.find(s[index]))
            index += 1
        return num_ops / 2


def run_tests():
    raw_inp = sys.stdin.readlines()[1:]
    formatted_inp = [s[:s.find('\n')] if '\n' in s else s for s in raw_inp]
    for test_case in formatted_inp:
        print get_num_ops(test_case)
        
run_tests()

