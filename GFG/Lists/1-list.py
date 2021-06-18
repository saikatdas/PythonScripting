'''
Lists in Python is used to store data at every index starting from 0. Lists  in Python works similarly to strings, it uses len() function to find the length, and it uses square brackets [ ] to access data.

For eg. if we have list arr = [1, 2, 3, 4, 5], then arr[0] = 1, arr[1] = 2, arr[2] = 3 and so on... Let's get it more clearly through the question below:

Given an array (list) of integers arr, the task is to check if first or last element in array arr is 0.

Example 1:

Input: 
N = 5 
arr = [0, 1, 2, 3, 0]
Output: 
Yes
Explanation: 
First and last element of list is 0,
so output is "Yes".
Example 2:

Input:
N = 6
arr = [2, 3, 4, 5, 1, 0]
Output: 
Yes
Explanation: 
Last element of list is 0,
so output is "Yes".
Your Task:
Your task is to complete the function check_zero(), which returns True if first or last element is 0, else returns False.

Constraints:
1 <= N <= 105
1 <= arr[i] <= 106
'''
#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3


# Function to check zero at 
# start and end index
def check_zero(N, arr):
    
    # complete the if statement to check
    # if first or last element in list is 0
    if(arr[0] == 0 or arr[N-1] == 0 ):
        return True

    return False

#{ 
#Driver Code Starts.

# Driver Code
def main():
    
    # Testcase input
    testcases = int(input())
    
    # Looping through testcases
    while(testcases > 0):
        # size of array
        N = int(input())
        
        # array elements input
        array = input().split()
        # print (array)
        arr = list()
        for i in array:
            arr.append(int(i))
            
        # print (arr)
        
        # calling function to check zero
        if(check_zero(N, arr) is True):
            print ("Yes")
        else:
            print ("No")
        
        testcases -= 1
 
if __name__ == '__main__':
    main()
#} Driver Code Ends