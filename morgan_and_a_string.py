"""
Jack and Daniel are friends. Both of them like letters, especially upper-case ones. 
They are cutting upper-case letters from newspapers, and each one of them has their 
collection of letters stored in separate stacks. 
One beautiful day, Morgan visited Jack and Daniel. He saw their collections. 
Morgan wondered what is the lexicographically minimal string, made of that two collections. 
He can take a letter from a collection when it is on the top of the stack. 
Also, Morgan wants to use all the letters in the boys' collections.

Input Format:

The first line contains the number of test cases, TT. 
Every next two lines have such format: the first line contains string AA, 
and the second line contains string BB.

Output Format:

Output the lexicographically minimal string S for each test case in new line.

Sample Input:

2
JACK
DANIEL
ABACABA
ABACABA

Sample Output:

DAJACKNIEL
AABABACABACABA
"""

from collections import deque
from builtins import range
from builtins import input

for _ in range(int(input())):
    a = input() + '['
    b = input() + '['
    string = deque()
    while len(a) > 1 and len(b) > 1:
        if a < b:
            string.append(a[0])
            a = a[1:]
        else:
            string.append(b[0])
            b = b[1:]
    print(''.join(string) + a[:-1] + b[:-1])