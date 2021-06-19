'''
Now, let's solve a question. Given a list arr of integers, the task is to print all elements till half of the length of list. Also, after half, print every third element of list (including the element just after half, if exists).

Example:

Input:  
N = 7 
arr = [1, 2, 3, 4, 5, 6, 7]
Output: 
1 2 3 4 7
Explanation:
1 2 3 is printed as it is till half
the length of list. After this, loop
for jump of three is started from 4, 
so 4 is the first element and next 
element is 7 (3rd index from 4).
Your Task:
Your task is to complete print_elements(), to print elements from list in required fashion.

Constraints:
6 <= N (length of arr) <= 104
1 <= arr[i] <= 106
Ref - https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/#:~:text=Without%20using%20loops%3A%20*%20symbol%20is,sep%3D%E2%80%9D%2C%20%E2%80%9D%20respectively.

'''
#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3

# Function to print list 
# print elements in required fashion
def print_elements(N, arr):
    
    # Your code here 
    # use '//' to divide to get int for index
    
    newList = []
    l = N // 2
    for i in range(l):
        newList.append(arr[i])
    
    for l in range(l,N,3):
        newList.append(arr[l])
    
    print(*newList, end=" ")

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
        
        # calling function to print elements
        print_elements(N, arr)
        print ()
        testcases -= 1
 
if __name__ == '__main__':
    main()
#} Driver Code Ends