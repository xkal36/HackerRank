"""
42 is the answer to "The Ultimate Question of Life, The Universe, and Everything". 
But what The Ultimate Question really is? We may never know!

Given three integers, a, b, and c, insert two operators between them so that the 
following equation is true: a (operator1) b (operator2) c = 42.

You may only use the addition (+) and multiplication (∗) operators. You can't change the order of the variables.

If a valid equation exists, print it; otherwise, print This is not the ultimate question.

Input Format

A single line consisting three space-separated integers: a, b, and c.

Constraints: 

0 <= a , b, c <= 42

Output Format:

Print the equation with no whitespace between the operators and the three numbers. 
If there is no answer, print This is not the ultimate question.

Note: It is guaranteed that there is no more than one valid equation per test case.

Sample Input

Example 1:

12 5 6

Example 2:

10 20 12

Example 3:

5 12 6

Sample Output

Example 1:

12+5*6

Example 2:

10+20+12

Example 3:

This is not the ultimate question
"""


import itertools
import sys


a, b, c = raw_input().strip().split(' ')
a, b, c = [int(a),int(b),int(c)]

def is_ultimate_question(x, y, z):
    operators = ['+', '*']
    for i in itertools.combinations_with_replacement(operators, 2):
        expression1 = (str(x) + '%s' + str(y) + '%s' + str(z)) % (i[0], i[1])
        expression2 = (str(x) + '%s' + str(y) + '%s' + str(z)) % (i[1], i[0])
        if eval(expression1) == 42:
            return expression1
        elif eval(expression2) == 42:
            return expression2
    return "This is not the ultimate question"

print is_ultimate_question(a, b, c)