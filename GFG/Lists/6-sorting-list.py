'''
Could you think of sorting a list of tuple according to your requirement. We can make this possible through custom sort in Python.

Syntax:

sorted(arr, key = compareSort)
arr is the list you want to sort, and compareSort is the function in which you need to write your comparator.

Example:

arr = [('a', 1), ('b', 2), ('c', 3),
       ('d', 4), (''e', 4)] 
we want to sort this list according to second value of tuple and if second value is same, then sort according to first value, then just mention the comparator as key in sort function and define that function with return value as the key according to which you want to sort the list.

Let's implement this out through a question. Given a list of tuples comprising name and marks of students. The task is to sort the students according to the marks, but wherever same marks is encountered, sort the two according to the name.

Example:

Input: 
N = 5 
arr = [[a, 100], [b, 100], [c, 300], 
[aad, 100], [abc, 100]]
Output: 
a 100 aad 100 abc 100 b 100 c 300 
Explanation:
First, list is sorted according to marks, 
and when marks are equal, then sorted 
according to the name.
Your Task:
Your task is to complete the comparator function customSort(), that takes arr as input, which compares as required and returns the required value.

Constraints:
1 <= N <= 104
1 <= marks <= 104
'''
#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3

# Function to sort using comparator
def last(n):
    return n[0]
def customSort(arr):
    
    return sorted(arr, key = last)
    

#{ 
#Driver Code Starts.
    
# Driver Code
def main():
    
    # Testcase input
    testcases = int(input())
    
    # Looping through testcases
    while(testcases > 0):
        N = int(input())
        
        name = input().split()
        marks = input().split()
        arr = list()
        for i in range(0, N, 1):
            arr.append((name[i], marks[i]))
        
        arr.sort(key = customSort)
        
        for i in arr:
            print (i[0], i[1], end = " ")
        
        print ()
        testcases -= 1
 
if __name__ == '__main__':
    main()
#} Driver Code Ends