"""
John has discovered various rocks. Each rock is composed of various elements, 
and each element is represented by a lower-case Latin letter from 'a' to 'z'. 
An element can be present multiple times in a rock. An element is called a gem-element 
if it occurs at least once in each of the rocks.

Given the list of N rocks with their compositions, display the number of gem-elements that exist in those rocks.

Input Format:

The first line consists of an integer, NN, the number of rocks. 
Each of the next NN lines contains a rock's composition. 
Each composition consists of lower-case letters of English alphabet.

Constraints: 
1 <= N <= 100

Each composition consists of only lower-case Latin letters ('a'-'z'). 
1 <= length of each composition <= 100

Output Format:

Print the number of gem-elements that are common in these rocks. If there are none, print 0.

Sample Input:

3
abcdde
baccd
eeabg

Sample Output:

2
"""


import string
import sys

def format_input():
    raw_inp = sys.stdin.readlines()[1:]
    formatted_inp = [s[:s.find('\n')] if '\n' in s else s for s in raw_inp]
    return formatted_inp

def get_num_gemstones(rock_elements):
    element_freqs = {letter: 0 for letter in string.lowercase}
    for item in rock_elements:
        already_counted = []
        for letter in item:
            if letter not in already_counted:
                element_freqs[letter] += 1
            already_counted.append(letter)
    num_common = 0
    for key in element_freqs:
        if element_freqs[key] == len(rock_elements):
            num_common += 1
    return num_common
    
print get_num_gemstones(format_input())