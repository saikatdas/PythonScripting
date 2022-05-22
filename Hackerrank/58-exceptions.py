"""
try catch block

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
