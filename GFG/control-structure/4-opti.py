#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3

    
def nearestPower(A, B):
    ##Your code here
    ##return the closest power
    
    # p = 2
    # v = A
    # prevValue = v
    # prevP = 2
    # while v < B:
        
    #     prevValue = v
    #     v = A ** p
    #     p = p + 1
    # return prevValue
    p = 0
    p = math.log(B,A)
    res = int(math.floor(p))
    
    return A ** res

#{ 
#Driver Code Starts.


import math

    
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        A = int(input())
        B = int(input())
        print(nearestPower(A, B))
        testcases-=1
        


if __name__=='__main__':
    main()
#} Driver Code Ends