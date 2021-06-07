'''
 In this question, we'll learn to print table by using the for loop.

You are given a number N, you need to print its multiplication table.

Note: Please go through the range function to understand why it's useful in for loops.

Example 1:

Input:
N = 5
Output:
5 10 15 20 25 30 35 40 45 50
'''
#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3


def multiplicationTable(N):## in is a membership operator that is true if something is a member of sequence
    for i in range(1,11,1): ## i in range(x,y,z) means i goes from x to y-1 and increments z steps in each iteration
        print(i * N, end=" ") ## Separating by spaces using end =" "
        

#{ 
#Driver Code Starts.


def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        N = int(input())
        multiplicationTable(N)
        print()
        testcases-=1
        


if __name__=='__main__':
    main()
#} Driver Code Ends