'''
Python functions allows us to create anonymous functions using the lambda keyword. These functions are small one line functions that don't use the def keyword.

In this question we will create an anonymous function to print a to power b.
Example:

Input: 
a = 6 
b = 2 
Output: 
36
Your Task:
This is a function problem. You don't need to take any input. Just complete the anonymous function power using lambda that print ab.

Constraints:
1 <= a, b <= 100
reference - https://www.w3schools.com/python/python_lambda.asp
'''
#{ 
#Driver Code Starts
#Initial Template for Python 3


 # } Driver Code Ends
#User function Template for python3


    
power =  lambda a, b : a ** b


#{ 
#Driver Code Starts.    
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        a = int(input())
        b = int(input())
        print(power(a, b)) ##calling the anonymous function
        testcases -= 1
        


if __name__=='__main__':
    main()
#} Driver Code Ends