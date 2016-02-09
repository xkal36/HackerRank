"""
Limak is a little bear who loves school. Today was his first lesson in cryptography, 
and the teacher assigned some difficult homework - to find any number with exactly K divisors. 
Limak wants to go the extra mile and find the biggest possible number; however, his 
teacher explained that there are arbitrarily large numbers with this property.

To give this little bear a more achievable challenge, the teacher advised him to consider only numbers not greater than N.

Given N and K, what is the largest number Limak can find?

Input Format:

The first line contains an integer, T (the number of test cases). 
The T subsequent lines of test cases each contain two space-separated integers, N and K, respectively.

Constraints: 

1 <= T <= 50
1 <= N <= 10**12
1 <= K <= 40

Output Format:

For each test case, print the biggest number Limak can find on a new line. Print −1 if no such number exists.

Sample Input:

3
15 3
15 4
15 5

Sample Output:

9
15
-1
"""


import resource
import sys

resource.setrlimit(resource.RLIMIT_STACK, (2**50,-1))
sys.setrecursionlimit(10**6)


T = int(raw_input().strip())
tests = []
for a0 in xrange(T):
    N,K = raw_input().strip().split(' ')
    N,K = [int(N),int(K)]
    tests.append((N, K))
    

def primes(n):
    if n<=2:
        return []
    sieve=[True]*(n+1)
    for x in range(3,int(n**0.5)+1,2):
        for y in range(3,(n//x)+1,2):
            sieve[(x*y)]=False

    return [2]+[i for i in range(3,n,2) if sieve[i]]



def factorize(n, primes):
    factors = []
    for p in primes:
        if p*p > n: break
        i = 0
        while n % p == 0:
            n //= p
            i+=1
        if i > 0:
            factors.append((p, i));
    if n > 1: factors.append((n, 1))

    return factors


def divisors(factors):
    div = [1]
    for (p, r) in factors:
        div = [d * p**e for d in div for e in range(r + 1)]
    return div

def get_largest_poss(N, K):   
    if N == 0:
        return -1
    elif len(divisors(factorize(N, primes(N)))) == K:
        return N
    else:
        return get_largest_poss(N -1, K)
    

for test in tests:
    N = test[0]
    K = test[1]
    print get_largest_poss(N, K)