"""
One of the built-in functions of Python is divmod, which takes two arguments a and b and returns a tuple containing the quotient of a//b first and then the remainder a.

Output Format
Print the result as described above.

Sample Input

177
10
Sample Output

17
7
(17, 7)

"""

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a%b)
    print(divmod(a,b))

