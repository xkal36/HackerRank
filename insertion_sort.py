"""
Given a sorted list with an unsorted number e in the rightmost cell, 
can you write some simple code to insert e into the array so that it remains sorted?

Print the array every time a value is shifted in the array until the array is fully sorted. 
The goal of this challenge is to follow the correct order of insertion sort.


Input Format:
There will be two lines of input:

Size - the size of the array
Arr - the unsorted array of integers

Output Format:
On each line, output the entire array every time an item is shifted in it.

Sample Input:

5
2 4 6 8 3

Sample Output:

2 4 6 8 8 
2 4 6 6 8 
2 4 4 6 8 
2 3 4 6 8 
"""


def insertionSort(ar):
    to_insert = ar[len(ar) - 1]
    inserted = False
    index = len(ar) - 2
    iters = 0
    while not inserted and iters < (len(ar) - 1): 
        if ar[index] > to_insert:
            ar[index + 1] = ar[index]
        elif ar[index] < to_insert:
            inserted = True
            ar[index + 1] = to_insert
        index -= 1
        iters += 1
        print " ".join(map(str, ar))
    if iters >= len(ar) - 1 and not inserted:
        if ar[0] > to_insert:
            ar[0] = to_insert
        else:
            ar[1] = to_insert
        print " ".join(map(str, ar))
        
    
        

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)