"""
Regex program detect float point number

So I can also handle this case using try catch block haha


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        try:
            s = float(input())

            if (s == 0):
                print(False)
                break
            print(True)
        except ValueError:
            print(False)

"""
import re
if __name__ == '__main__':
    n =int(input())
    for _ in range(n):
        s = input()
        print(bool(re.search(r'^[-+]?[0-9]*\.[0-9]+$',s)))


