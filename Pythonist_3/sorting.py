"""
You are given a string S. 

S contains alphanumeric characters only. 

Your task is to sort the string S in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.

Input Format:

A single line of input contains the string SS.

Constraints:

0 < len(S) < 1000

Output Format:

Output the sorted string S.

Sample Input:

Sorting1234

Sample Output:

ginortS1324

Note: 
a) Using join, for or while anywhere in your code, even as substrings, will result in a score of 0. 
b) You can only use oneone sorted function in your code. A 0 score will be awarded for using sorted more than once. 
"""


def weird_sort(s, l=[], u=[], o=[], e=[]):
    if len(s) == 0:
        return reduce(lambda x, y: x+y, reduce(lambda x, y: x+y, map(sorted, [l] + [u] + [o] +  [e])))
    else:
        el = s[0]
        if el.istitle():
            u.append(el)
        elif el.islower():
            l.append(el)
        elif el.isdigit() and int(el) % 2 != 0:
            o.append(el)
        elif el.isdigit() and int(el) % 2 == 0:
            e.append(el)
    return weird_sort(s[1:], l, u, o, e)
        
print weird_sort(raw_input())  