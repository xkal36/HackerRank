"""
You have a record of N students. Each record contains the student's name, 
and their percent marks in Maths, Physics and Chemistry. 
The marks can be floating values. The user enters some integer N 
followed by the names and marks for NN students. You are required to 
save the record in a dictionary data type. The user then enters a student's name. 
Output the average percentage marks obtained by that student, correct to two decimal places.

Input Format:
The first line contains the integer N, the number of students. 
The next N lines contains the name and marks obtained by that student 
separated by a space. The final line contains the name of a particular student previously listed.

Output Format:
Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

Constraints 
2 <= N <= 10 
0 <= Marks <= 100

Sample Input:

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Sample Output:

56.00
"""

import sys

def query_records():
    results = {}
    num_students = int(raw_input())
    for i in range(num_students):
        info = raw_input()
        results[info[:info.find(' ')]] = map(float, info[info.find(' ') + 1:].split(' '))
    student = raw_input()
    return "%0.2f" % ((sum(results[student]) + 0.0) / len(results[student]))
         
        
        
print query_records()