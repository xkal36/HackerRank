"""
Neo has a complex matrix script. The matrix script is a N X M grid of strings. 
It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&).

To decode the script, Neo needs to read each column and select only the alphanumeric 
characters and connect them. Neo reads the column from top to bottom and starts reading from the leftmost column.

If there are symbols or spaces between two alphanumeric characters of the decoded script, 
then Neo replaces them with a single space '  ' for better readability.

Neo feels that there is no need to use 'if' conditions for decoding.

Alphanumeric characters consist of: [A-Z, a-z, and 0-9].

Input Format:

The first line contains space-separated integers N (rows) and M (columns) respectively. 
The next N lines contain the row elements of the matrix script.

Constraints:

0 < N, M < 100

Note: A 0 score will be awarded for using 'if' conditions in your code.

Output Format:

Print the decoded matrix script.
"""


import re
import sys



def decode_matrix(num_cols, num_rows, matrix):
    par_dec = []
    for i in range(num_cols):
        for mat in matrix:
            par_dec.append(mat[i])
    last_lett_ind = filter(lambda i: par_dec[i].isalnum(), [i for i in range(len(par_dec))])[-1]
    
    return re.sub(r'\W+', ' ', ''.join(par_dec[:last_lett_ind + 1])) + ''.join(par_dec[last_lett_ind + 1:])

info = raw_input()
rows = int(info[0])
cols = int(info[2])

matr = []
for i in range(rows):
    matr.append(raw_input())

print decode_matrix(cols, rows, matr)