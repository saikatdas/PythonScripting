"""
>>> from itertools import combinations
>>>
>>> print list(combinations('12345',2))
[('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]
>>>
>>> A = [1,1,3,3,3]
>>> print list(combinations(A,4))
[(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]


Sample Input

HACK 2
Sample Output

A
C
H
K
AC
AH
AK
CH
CK
HK
"""
from itertools import combinations
if __name__ == '__main__':
    s = input().split()
    strInput = sorted(s[0])
    k = int(s[1])
   
    for i in range(1,k+1):
        x = list(combinations(strInput,i))
        for e in x:
            print(''.join(e))
