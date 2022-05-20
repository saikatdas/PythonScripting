"""
>>> from collections import namedtuple
>>> Car = namedtuple('Car','Price Mileage Colour Class')
>>> xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
>>> print xyz
Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
>>> print xyz.Class
Y

Note:
1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet.
2. Column names are ID, MARKS, CLASS and NAME. (The spelling and case type of these names won't change.)

Sample Input

TESTCASE 01

5
ID         MARKS      NAME       CLASS
1          97         Raymond    7
2          50         Steven     4
3          91         Adrian     9
4          72         Stewart    5
5          80         Peter      6
TESTCASE 02

5
MARKS      CLASS      NAME       ID
92         2          Calum      1
82         5          Scott      2
94         2          Jason      3
55         8          Glenn      4
82         2          Fergus     5
Sample Output

TESTCASE 01

78.00
TESTCASE 02

81.00
"""
from collections import namedtuple
if __name__ == '__main__':
    sumMark = 0
    n = int(input())
    s = input().split()
    students = namedtuple('student',s)
    for _ in range(n):
        f1,f2,f3,f4 = input().split()
        student = students(f1,f2,f3,f4)
        sumMark += int(student.MARKS)
    avgMark = sumMark / n    
    print(format(avgMark,".2f"))
