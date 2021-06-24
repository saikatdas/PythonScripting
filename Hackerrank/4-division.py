'''
Task
The provided code stub reads two integers, a and b, from STDIN.

Add logic to print two lines. The first line should contain the result of integer division, a // b. The second line should contain the result of float division, a / b.

No rounding or formatting is necessary.

Example
Sample Input 0

4
3
Sample Output 0

1
1.33333333333.
'''
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)

