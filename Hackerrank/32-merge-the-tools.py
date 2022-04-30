"""
sample Input (remove duplicate from substring)
Task 1 - create substring
Task 2 - remove duplicate from substring

STDIN       Function
-----       --------
AABCAAADA   s = 'AABCAAADA'
3           k = 3
Sample Output

AB
CA
AD
"""

def removeDublicateSubStr(s):
    x = list(s)
    p = list(dict.fromkeys(x))
    y = ''.join(p)
    return y

def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        j = k + i
        subStr = string[i:j]
        uniqueStr = removeDublicateSubStr(subStr)
        print(uniqueStr)
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)