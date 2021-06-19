'''
a. list.append(element) : adds a single element to the end of the list. Doesn't return new list, modifies the original.
b. list.insert(index, element) : inserts the element at the given index, shifting elements to the right.
c. list.extend(list2) : adds the element in list2 to the end of the list. You can also use '+' to extend.
d. list.index(element) : searches for the given element from the start of the list and returns its index.
e. list.remove(element) : searches for the first instance of the given element and removes it.
f. list.sort() : sorts the list in place. (does not return anything)
g. list.reverse() : reverses the list in place. (does not return anything)
h. list.pop(index) : removes and returns the element at the given index, if index not found, returns the last element
i. string.join(list) : function to join the list elements using string as delimiter.

Now, let's try to solve a question. Given a list of string, the task is to perform Q operations on it.


insert_arr(): insert 'element' at index 'index'
pop_arr(): pop from index 'index'
rev_arr(): reverse the list
sort_arr(): sort the list
join_list(): join and print the elements of the list using string as delimiter.

Example:

Input: 
N = 5, Q = 3 
arr = [1, 2, 3, 4, 5]
Q1 = insert 0 at index 0
Q2 = reverse array
Q3 = print the elements with separator '#'
Output:
5#4#3#2#1#0 
5 4 3 2 1 0
Explanation: 
First operation to be performed is to 
insert 0, now list is as 1, 2, 3, 4, 5, 0.
Now, reversing the array we have 
5, 4, 3, 2, 1, 0. After this, printing the
element with separator '#', 5#4#3#2#1#0.
Your Task:
Your task is to complete different available functions insert_arr(), pop_arr(), rev_arr(), sort_arr(), and join_list(). to perform different operations on the given list.

Constraints:
1 <= N, arr[i] <= 104
1 <= Q <= 10
'''
#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3

# Function to sort the list
def sort_arr(arr):
    
    return arr.sort()
    
    # Your code here

# Function to join list elements
# with string as delimiter

def join_list(arr, string):
    # Complete the return statement to join list
    return  string.join(arr)

# Function to reverse array elements
def rev_arr(arr):
    # Your code here
    return arr.reverse()

# Function to insert element at index
def insert_arr(arr, index, element):
    # Your code here
    return arr.insert(index,element)
# Function to pop element from array at index
def pop_arr(arr, index):
    # Your code here
    return arr.pop(index)
#{ 
#Driver Code Starts.
# Driver Code
def main():
    
    # Testcase input
    testcases = int(input())
    
    # Looping through testcases
    while(testcases > 0):
        # size of array and query
        N_and_Q = input().split()
        N = int(N_and_Q[0])
        Q = int(N_and_Q[1])
        
        # array elements input
        array = input().split()
        
        arr = list()
        for i in array:
            arr.append(i)
        
        # looping through each query
        for i in range(0, Q, 1):
            query = input().split()
            op = query[0]
            
            if(op == 'i'):
                index = int(query[1])
                element = query[2]
                insert_arr(arr, index, element)
                
            if(op == 'p'):
                index = int(query[1])
                pop_arr(arr, index)
            
            if(op == 'j'):
                string = query[1]
                print (join_list(arr, string))
                
            if(op == 'r'):
                rev_arr(arr)
            
            if(op == 's'):
                sort_arr(arr)
                
        for i in arr:
            print (i, end= ' ')
        
        print ()
        
        testcases -= 1
 
if __name__ == '__main__':
    main()
#} Driver Code Ends