"""
You are given an integer, N. Your task is to print an alphabet rangoli of size N. 
(Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

#size 10

------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------

The center of the rangoli has the first alphabet letter a, and the boundary has the Nth alphabet letter (in alphabetical order).

Input Format

Only one line of input containing N, the size of the rangoli.

Constraints:

0 < N < 27

Output Format:

Print the alphabet rangoli in the format explained above.

Sample Input:

5

Sample Output:

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
"""


import os
import string
import sys

def get_input():
    return int(sys.stdin.readlines()[0])


def make_rangoli(width):
    alphabet = string.ascii_lowercase
    letters = alphabet[:width][::-1]
    
    num_lines = width * 2 - 1   
    centre = num_lines / 2
    offset = num_lines - 2 * centre
 
    if offset == 1:
        centre = centre + 1
    
    for line_d in range(1, num_lines + 1, 1):
        
        spaces = centre - line_d
        if spaces < 0:
            spaces = spaces * -1
        num_chars = 2 * (centre - spaces) - 1
        diamond = ""
        
        for l in range(0, spaces, 1):
            diamond = diamond + "--"
        diamond = diamond[:-1]
        
        if num_chars != num_lines:
            for q in range(0, num_chars, 1):
                diamond = diamond + "-%s" % letters[0]
        else:
            li = ['a' for i in range(num_lines + 1)]
            diamond += '-'.join(li)[:-1]
        
        if num_chars == num_lines:
            diamond = diamond[:-1]
        
        for l in range(0, spaces, 1):
            diamond = diamond + "--" 
        print diamond

make_rangoli(get_input())