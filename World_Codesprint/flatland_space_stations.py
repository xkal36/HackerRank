"""
Flatland is a country with nn cities, m of which have space stations. 
Its cities (c) are numbered from 0 to n−1, where ithith city is referred to as ci.

Between each ci and ci+1 (where 0 <= i < n), there exists a bidirectional road 1 km long.

For each city, determine its distance to the nearest space station and print the maximum of these distances.

Input Format:

The first line consists of two space-separated integers, n and m . 
The second line contains mm space-separated integers c0,c1,...cm−1
 denoting the index of each city having a space station. These values are unordered and unique.

Constraints:

1 <= n <= 10**5
1 <= m <= n

Note: There will be at least 11 city with a space station, and no city has more than one.

Output Format

Print an integer denoting the maximum distance that an astronaut in a Flatland city 
would need to travel to reach the nearest space station.

Sample Input 1

5 2
0 4

Input Output 1

2

Sample Input 2

6 6
0 1 2 4 3 5

Input Output 2

0
"""


import sys


n, m = raw_input().strip().split(' ')
n, m = [int(n),int(m)]
c = map(int,raw_input().strip().split(' '))

def get_closest_num(l, num):
    low = 0
    high = len(l) - 1
    
    while low < high:
        mid = (low + high) / 2
        d1 = abs(l[mid] - num)
        d2 = abs(l[mid + 1] - num)
        if d2 <= d1:
            low = mid + 1
        else:
            high = mid
    return l[high]

all_cities = range(n)
c = sorted(c)
all_nearest_dists = [abs(num - get_closest_num(c, num)) for num in all_cities]
print max(all_nearest_dists)