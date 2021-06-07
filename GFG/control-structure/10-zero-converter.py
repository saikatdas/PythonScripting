'''
You are given a number n. The number n can be negative or positive. If n is negative, print numbers from n to 0 by adding 1 to n. If positive, print numbers from n-1 to 0 by subtracting 1 from n.

Example 1:

Input:
n = 0
Output:
already Zero
Example 2:

Input:
n = 4
Output:
3 2 1 0
Example 3:

Input:
n = -3
Output:
-3 -2 -1 0
'''

#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3

def pos(n):
    
    while n >= 0:
        n = n - 1
        if n >= 0:
            print(n, end = " ")
        
        
    
def neg(n):
    while n <= 0:
        print(n, end = " ")
    
        n = n + 1

    

#{ 
#Driver Code Starts.


def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        n = int(input())
        if(n > 0):
            pos(n)
        elif(n < 0):
            neg(n)
        else:
            print("already Zero",end="")
        print()
        testcases-=1
        


if __name__=='__main__':
    main()
#} Driver Code Ends