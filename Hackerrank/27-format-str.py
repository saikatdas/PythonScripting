"""
Sample Input - 17


Sample Output

    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001

   n = int(raw_input())
spacing = len(bin(n)[2:])

for i in range(1,n+1):
    print str(i).rjust(spacing, ' '),str(oct(i)[1:]).rjust(spacing, ' '),str(hex(i)[2:].upper()).rjust(spacing, ' '),str(bin(i)[2:]).rjust(spacing, ' ')


  https://www.w3schools.com/python/ref_string_format.asp

"""

def print_formatted(number):
    # your code goes here
    
    for i in range(1,number+1):
        # d = str(i)
        # o = oct(i)[2:]
        # X = hex(i)[2:].upper()
        # b = bin(i)[2:]
        width = len("{0:b}".format(n)) #max binary digits
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))
     

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)