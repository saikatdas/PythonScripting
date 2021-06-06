'''
Bitwise operators are useful when we want to work with bits. Here, we'll take a look at them.
Given three positive integers a, b and c. Your task is to perform some bitwise operations on them as given below:


1. d = a ^ a
2. e = c ^ b
3. f = a & b
4. g = c | (a ^ a)
5. e = ~ e
Note: ^ is for xor
'''
#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3


def bitwise(a, b, c):
    
    l = a ^ a
    m = c ^ b
    n = a & b
    o = (c | (a ^ a))
    p = ~ m
    print(l)
    print(m)
    print(n)
    print(o)
    print(p)

#{ 
#Driver Code Starts.



def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        a = int(input())
        b = int(input())
        c = int(input())
        bitwise(a, b, c)
        testcases-=1
        


if __name__=='__main__':
    main()
#} Driver Code Ends