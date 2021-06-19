'''
Great...! You are now up with various inbuilt functions in Python List. Now, the time is to get introduced to some other useful functions, described below:
a. sum(list) : returns the sum of all elements in the list.
b. min(list) : returns the minimum element from the list.
c. max(list) : return the maximum element from the list.

Now, let's use these methods through a question. Given a list arr of integers, the task is to find the average of all elements in the list, ignoring the minimum and maximum from the list. If more than one copy of minimum and maximum element exists, ignore one.

Example:

Input:
N = 5 
arr = [6, 4, 8, 12, 3]
Output: 
6
Explanation: 
Minimum element in the list is 3 and
maximum is 12, so average excluding 
min and max is 18 / 3 = 6.
Your Task:
Your task is to complete the function calc_average(), that takes arr as input, and returns the required average.

Constraints:
3 <= N <= 104
1 <= arr[i] <= 104
'''
#User function Template for python3

# Function to calculate average
def calc_average(arr):
    # Your code here
    l = len(arr)
    
    totalSum = sum(arr)
    countMax = arr.count(max(arr))
    countMin = arr.count(min(arr))
    l = l - countMax - countMin
    
    mySum = totalSum - max(arr) - min(arr)
    
    avg = mySum // l
    return avg
#{ 
#  Driver Code Starts
#Initial Template for Python 3


# Driver Code
if __name__ == '__main__':
    # Testcase input
    testcases = int(input())
    # Looping through testcases
    while(testcases > 0):
        N = int(input())
        
        a = list(map(int,input().strip().split()))
        
        print (calc_average(a))
        
        testcases -= 1
# } Driver Code Ends