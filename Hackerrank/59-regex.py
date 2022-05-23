"""
Sample Input

2
.*\+
.*+
Sample Output

True
False
Explanation

.*\+ : Valid regex.
.*+: Has the error multiple repeat. Hence, it is invalid

"""

import re

if __name__ =='__main__':
    
    for _ in range(int(input())):
        try:
            re.compile(input())
            print('True')
        except re.error:
            print('False')
            continue
        