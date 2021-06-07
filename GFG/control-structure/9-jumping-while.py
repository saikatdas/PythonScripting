'''
Let's get deeper into understanding it through below question.

Given a positive integer x, the task is to print the numbers from 1 to x in the order as 12, 22, 32, 42, 52, ... (in increasing order).

Example:

Input:
x = 10
Output:
1 4 9
Explanation:
From 1 to 10, numbers in powers
of 2 are, 12, 22, 32 as 1, 4 and 9.
'''
#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3

# Function to print x in increasing order
def printIncreasingPower(x):
    ##Your code here
    
    i = 1
    p = i
    while(p <= x):
        
        p = i ** 2
        if p <= x:
            print ( p, end = " " )
        
        i += 1

#{ 
#Driver Code Starts.
# Driver Code
def main():
    
    # Testcase input
    testcases = int(input())
    
    # Looping through testcases
    while(testcases > 0):
        x = int(input())
        
        printIncreasingPower(x);
        print ()
        
        
        testcases -= 1
 
if __name__ == '__main__':
    main()
#} Driver Code Ends