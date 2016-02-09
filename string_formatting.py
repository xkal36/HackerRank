"""
Task:
Read the integer, N and print the decimal, 
octal, hexadecimal, and binary values 
from 1 to N with space padding so that all 
fields take the same width as the binary value.

Input Format:
The first line contains an integer, NN.

Constraints:
1 <= N <= 991 <= N <= 99

Output Format:
Print N lines. Format the fields as the width of the binary value of N.
"""

n = int(raw_input())
width = len("{0:b}".format(n))
for i in xrange(1, n+1):
  print "{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width)