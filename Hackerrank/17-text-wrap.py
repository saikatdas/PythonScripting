'''
You are given a string S and W width .
Your task is to wrap the string into a paragraph of W width .
Sample Input 0

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Sample Output 0

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
'''

#using textwrap
#return "\n".join(textwrap.wrap(string, max_width))
import textwrap

def wrap(string, max_width):  #not using textwrap
    i = 0
    l =len(string)
    myStr = ''
    for e in range(i,l,max_width):
        if ( i + max_width > l):
            # print(i,l)
            # print(string[i:l])
            myStr += string[i:l] 
            break
        # print(i,i + max_width)
        # print(string[i:i + max_width])
        myStr += string[i:i + max_width] + '\n'
        i += max_width
    return myStr

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)