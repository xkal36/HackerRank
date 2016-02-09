"""
Mr. Vincent works in a door mat manufacturing company. 
One day, he designed a new door mat with the following specifications:

1. Mat size must be N X M. (N is an odd natural number, and M is 33 times N.)

2. The design should have 'WELCOME' written in the center.
3. The design pattern should only use |, . and - characters.


Input Format:
A single line containing the space separated values of NN and MM.

Constraints:
5 < N < 1015 < N < 101
15 < M < 30315 < M < 303

Output Format:
Output the design pattern.

Sample Input:
9 27

Sample Output:

------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
"""


import sys

if sys.version_info[0] >= 3: 
	raw_input=input

N, M = map(int,raw_input().split())

a=[('.|.'*i).center(M,'-') for i in range(1, N, 2)]

for e in a + ['WELCOME'.center(M,'-')] + list(reversed(a)):
	printe