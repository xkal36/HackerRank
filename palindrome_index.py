"""
Given a string of lowercase letters, determine the index of 
the character whose removal will make the string a palindrome. 
If the string is already a palindrome, then print −1. There will always be a valid solution.

Input Format:

The first line contains T (the number of test cases). 
The T subsequent lines of test cases each contain a single string to be checked.

Constraints 
1 <= T <= 20
1 <= length of string <= 100005
All characters are Latin lower case indexed.

Output Format:

Print the zero-indexed position (integer) of a character whose deletion will result in a palindrome; 
if there is no such character (i.e.: the string is already a palindrome), print -1. 
Any correct answer will be accepted; e.g.: for a string such as bcbc, we can either remove b 
at index 0 or c at index 3— both answers are acceptable.

Sample Input:

3
aaab
baa
aaa

Sample Output:

3
0
-1
"""


import sys

# Inefficient solution:
def get_index_slow(s):
    if s == s[::-1]:
        return -1
    else:
        is_palindrome = False
        index = 0
        s_list = s
        while not is_palindrome:
            if  s_list[:index] + s_list[index + 1:] == (s_list[:index] + s_list[index + 1:])[::-1]:
                is_palindrome = True
            else:
                index += 1
        return index

# Efficient solution:
def get_index(s):
    if s == s[::-1]:
        return -1
    else:
        length_s = len(s) 
        index = 0
        while True:
            if s[index] != s[(length_s - 1) - index]:
                if  s[:index] + s[index + 1:] == (s[:index] + s[index + 1:])[::-1]:
                    return index
                else:
                    return (length_s - 1) - index
            index += 1

def run_tests():
    raw_inp = sys.stdin.readlines()[1:]
    formatted_inp = [s[:s.find('\n')] if '\n' in s else s for s in raw_inp]
    for test_case in formatted_inp:
        print get_index(test_case)
        
run_tests()