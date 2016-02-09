"""
Sami's spaceship crashed on Mars! She sends nn sequential SOS messages to Earth for help.

Letters in some of the SOS messages are altered by cosmic radiation during transmission. 
Given the signal received by Earth as a string, S, determine how many letters of Sami's SOS have been changed by radiation.

Input Format

There is one line of input: a single string, S.

Note: As the original message is just SOS repeated n times, S's length will be a multiple of 3.

Constraints:

1 <= |S| <= 99
|S| % 3 = 0
S will contain only uppercase English letters.

Output Format:

Print the number of letters in Sami's message that were altered by cosmic radiation.

Sample Input 1

SOSSPSSQSSOR

Sample Output 1

3

Sample Input 2

SOSSOT

Sample Output 2

1
"""


import sys


S = raw_input().strip()

def count_changes(s):
    signal_len = len(s)
    expected = 'SOS' * (signal_len / 3)
    count = 0
    for i in range(signal_len):
        if expected[i] != s[i]:
            count += 1
    return count

print count_changes(S)