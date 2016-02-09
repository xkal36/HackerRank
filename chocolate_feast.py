"""
Little Bob loves chocolate, and he goes to a store with $Nin his pocket. 
The price of each chocolate is $C. The store offers a discount: 
for every M wrappers he gives to the store, he gets one chocolate for free. 
How many chocolates does Bob get to eat?

Input Format: 
The first line contains the number of test cases, T. 
TT lines follow, each of which contains three integers, N, C, and M.

Output Format: 
Print the total number of chocolates Bob eats.

Sample input:

3
10 2 5
12 4 4
6 2 2

Sample Output:

6
3
5
"""

import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        N, C, M = list(int(x) for x in sys.stdin.readline().split())
        
        total = N // C
        wrappers = total
        
        while wrappers >= M:
            wrappers += 1 - M
            total += 1
        
        print total