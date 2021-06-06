'''
Logical operators are and, or, not. They are used in condition checking.


Example: a and b checks if both a and b are True. First a is checked then b.
a or b checks if either of a or b is True. If one is True; it doesn't check for other.
not a complements the boolean value of a


Note: 0 and empty string are False and all other values are True.
'''
#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3

def logical(a, b):
    print(a and b) ## do a and b
    print(a or b) ## do a or b
    print(not a) ## do not a


#{ 
#Driver Code Starts.


def main():
    testcases =  int(input()) #testcases
    while(testcases>0):
        a = int(input())
        b = int(input())
        logical(a, b)
        testcases-=1
        


if __name__=='__main__':
    main()
#} Driver Code Ends