"""
You are given a list of N lowercase English letters. For a given integer K, 
you can select any K indices (assume 11-based indexing) with a uniform probability from the list.

Find the probability that at least one of the K indices selected will contain the letter: 'a'.

Input Format:

The input consists of three lines. The first line contains the integer N, 
denoting the length of the list. The next line consists of N space-separated lowercase English letters, 
denoting the elements of the list.

The third and the last line of input contains the integer KK, denoting the number of indices to be selected.

Output Format:

Output a single line consisting of the probability that at least one of the K indices selected contains the letter: 'a'.

Note: The answer must be correct up to 3 decimal places.

Constraints

1 <= N <= 10
1 <= K <= N
All the letters in the list are lowercase English letters.

Sample Input:

4 
a a c d
2

Sample Output:

0.8333
"""


import itertools
import sys


def get_prob(l, k):
    list_l = l.split()
    a_indexes = [i for i in range(len(list_l)) if list_l[i] == 'a']
    all_poss_indices = list(itertools.combinations(range(len(list_l)), int(k)))
    count = 0
    for comb in all_poss_indices:
        for ind in a_indexes:
            if ind in comb:
                count += 1
                break
    return (count + 0.0) / len(all_poss_indices)
     

n = raw_input()
lst = raw_input()
num = raw_input()

print get_prob(lst, num)
