'''
Python functions allow us to take variable arguments. The parameter that takes variable argument has a * as prefix.

In this question we will sum the elements taken as variable arguments and print the result.

Examples:

Input: 
n = 6
*var =  4, 5, 6, 7
Output: 
28
Your Task:
This is a function problem. You don't need to take any input. Just complete the function multivar(), that print the sum of n with elements of variable argument.

Constraints:
1 <= n <= 103
Reference - https://www.geeksforgeeks.org/args-kwargs-python/
'''
#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3


def multivar(n, *var): 
    ##*var takes multiple arguments inside it
    ##print the sum of a+elements of var
    res = 0
    v = 0
    for v in var:
        res += v
    print(n + res)
#{ 
#Driver Code Starts.


def main():
    testcases=int(input()) #testcases
    while(testcases > 0):
        single = int(input())
        multivar(single, 4, 5, 6, 7) ## The single argument and multiarguments are passed to multivar function
        testcases -= 1
        


if __name__=='__main__':
    main()
#} Driver Code Ends