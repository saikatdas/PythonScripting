"""
Sample Input

1 4
x**3 + x**2 + x + 1
Sample Output

True

use eval : eval needs a variable named x to be defined
If you don't have a variable named x , you will get an error

https://stackoverflow.com/questions/494594/how-to-write-the-fibonacci-sequence

"""

if __name__ == '__main__':
    x,k=map(int, input().split())
    print (k==eval(input()))
