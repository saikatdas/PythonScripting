"""
phone number should starts with 7,8 or 9 , total 10 digit
2
9587456281
1252478965
Sample Output

YES
NO
"""
import re

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        if (bool(re.search(r"^[789][0-9]{9}$",input()))):
            print('YES')
        else:
            print('NO')
