"""
You and Fredrick are good friends. Yesterday, Fredrick received N credit cards from ABCD Bank. 
He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!

A valid credit card from ABCD Bank has the following characteristics: 

It must start with a 44, 55 or 66. 
It must contain exactly 1616 digits. 
It must only consist of digits (00-99). 
It may have digits in groups of 44, separated by one hyphen "-". 
It must NOT use any other separator like '   ' , '_', etc. 
It must NOT have 44 or more consecutive repeated digits.

Examples:

Valid Credit Card Numbers

4253625879615786
4424424424442444
5122-2368-7954-3214

Invalid Credit Card Numbers

42536258796157867       #17 digits in card number → Invalid 
4424444424442444        #Consecutive digits are repeating 4 or more times → Invalid
5122-2368-7954 - 3214   #Separators other than '-' are used → Invalid
44244x4424442444        #Contains non digit characters → Invalid
0525362587961578        #Doesn't start with 4, 5 or 6 → Invalid

Input Format:

The first line of input contains an integer N. 
The next N lines contain credit card numbers.

Constraints:

0 < N < 100

Output Format:

Print 'Valid' if the credit card number is valid. Otherwise, print 'Invalid'. Do not print the quotes.

Sample Input:

6
4123456789123456
5123-4567-8912-3456
61234-567-8912-3456
4123356789123456
5133-3367-8912-3456
5123 - 3567 - 8912 - 3456

Sample Output:

Valid
Valid
Invalid
Valid
Invalid
Invalid
"""


import itertools
import sys

def get_input():
    raw_inp = sys.stdin.readlines()[1:]
    form_inp = [s[:s.find('\n')] if '\n' in s else s for s in raw_inp]
    return form_inp


def conseqs_over_four(s):
    cons = []
    list_s = filter(lambda ch: ch.isdigit(), list(s))
    for x, v in itertools.groupby(list_s):
        cons.append(list(v))
    for con in cons:
        if len(con) >= 4:
            return True
    return False

def validate_card(card_no):
    # check if fstarts with 4, 5 or 6
    if card_no[0] not in ['4', '5', '6']:
        return 'Invalid'
    
    # check if num digits is 16
    num_digits = 0
    for ch in card_no:
        if ch.isdigit():
            num_digits += 1
    if num_digits != 16:
        return 'Invalid'
    
    # check if any unallowed chars or digits
    allowed = '0123456789-'
    for ch in card_no:
        if ch not in allowed:
            return 'Invalid'
    # check if a ch appears over 4 time consecutively
    if conseqs_over_four(card_no):
        return 'Invalid'
    
    # check if all groups have len 4
    if '-' in card_no:
        groups = card_no.split('-')
        for group in groups:
            if len(group) != 4:
                return 'Invalid'
    
    return 'Valid'
    
    

for card in get_input():
    print validate_card(card)