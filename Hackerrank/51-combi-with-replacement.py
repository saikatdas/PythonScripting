"""
This tool returns r length subsequences of elements from the input iterable allowing individual elements to be repeated more than once.

Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

Sample Input

HACK 2
Sample Output

AA
AC
AH
AK
CC
CH
CK
HH
HK
KK

"""
from itertools import combinations_with_replacement
if __name__ == '__main__':
    s, k = input().split()
    t = list(combinations_with_replacement(sorted(s),int(k)))
    for e in t:
        print(''.join(e))
    