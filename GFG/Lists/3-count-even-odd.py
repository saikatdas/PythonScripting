'''
Given a list arr of positive integers. The task is to count the number of even elements and odd elements in this list.

Example:

Input:
N = 7 
arr = [1, 2, 3, 4, 5, 6, 7]
Output: 
3 4
Explanation: 
In the given list, there are 3 even numbers  
(2, 4, 6) and 4 odd elements (1, 3, 5, 7).
Your Task:
Your task is to complete the function count_even_odd() which should returns a list (you can use append() method in list to add elements) in which first element as count of even and second element as count of odd .

Constraints:
1 <= N <= 106
1 <= arr[i] <= 106
'''
#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3

# Function to count even and odd
# c_e : variable to store even count
# c_o : variable to store odd count
#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3

# Function to count even and odd
# c_e : variable to store even count
# c_o : variable to store odd count
def count_even_odd(N, arr):
    
    i = 0
    c_e = 0
    c_o = 0
    
    pair = [] # u can also declaire it pair = list()
    
    
    # your code here
    for i in range(i,len(arr),1):
        if (arr[i] % 2 == 0):
            c_e += 1
        else:
            c_o += 1
    pair.append(c_e)
    pair.append(c_o)
    return pair

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
        
        # calling function to count even odd
        a = count_even_odd(N, arr)
        print (a[0], a[1])
        testcases -= 1
 
if __name__ == '__main__':
    main()
#} Driver Code Ends