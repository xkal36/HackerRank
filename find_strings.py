"""
You are given n strings w1, w2, ......, wn. Let Si 
denote the set of strings formed by considering all 
unique substrings of the string wi. A substring is defined 
as a contiguous sequence of one or more characters in the string. M
Let S = {S1 U S2 U .... Sn} .i.e S is a set of strings formed by 
considering all the unique strings in all sets S1, S2, ..... Sn. 
You will be given many queries, and for each query, you will be 
given an integer 'k'. Your task is to display the lexicographically 
kth smallest string from the set S.

Input:
The first line of input contains a single integer n, 
denoting the number of strings. Each of the next n lines 
consists of a string. The string on the ith line (1 <= i <= n) 
is denoted by wi and has a length mi. The next line consists 
of a single integer q, denoting the number of queries. 
Each of the next q lines consists of a single integer k.

Note: The input strings consist only of lowercase english alphabets 'a' - 'z'.

Output:

Output q lines, where the ith line consists of a string which 
is the answer to the ith query. If the input is invalid (i.e., k > size of S), 
display "INVALID" for that case.

Constraints:

1<= n <=50 
1<= mi <=2000 
1<= q <=500 
1<= k <=1000000000

Sample Input: 

2 
aab 
aac 
3 
3 
8 
23

Sample Output: 

aab 
c 
INVALID
"""


import itertools
import sys

def substrings(s):
    for i, j in itertools.combinations(xrange(len(s)+1), 2):
        yield s[i:j]


def find_string(sts, k):
    subs = [substrings(st) for st in sts]
    subs_unique = [list(set([''.join(c) for c in sub])) for sub in subs]
    
    subs_union = set().union(*subs_unique)
    subs_union_len = len(subs_union)
    sorted_subs_union = sorted(list(subs_union))
    
    if k <= subs_union_len:
        return sorted_subs_union[k - 1]
    else:
        return 'INVALID'
    
       

def run_tests():
    raw_inp = sys.stdin.readlines()
    formatted_inp = [s[:s.find('\n')] if '\n' in s else s for s in raw_inp]
    sts = formatted_inp[1:int(formatted_inp[0]) + 1]
    k_array = map(int, formatted_inp[int(formatted_inp[0]) + 1:])
    for i in range(len(k_array) - 1):
        print find_string(sts, k_array[1:][i])

run_tests() 