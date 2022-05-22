"""
try catch block

Sample Input

3
1 0
2 $
3 1
Sample Output

Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'
3

"""
if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        d = input().split()
        try:
            r = int(d[0]) // int(d[1])
            print(r)
        except (ZeroDivisionError,ValueError) as e:
            print("Error Code:",e)
