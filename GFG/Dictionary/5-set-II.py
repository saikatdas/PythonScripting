'''
union(): Used to find union() between two sets. It performs this using '|' operator.
intersection(): Used to find intersection() between two sets. It performs this using '&' operator.
difference(): Difference of A and B (A - B) is a set of elements that are only in A but not in B. Similarly for B - A holds the same.

Now, Given some elements in two sets a and b, the task is to find the elements common in two sets, elements in both the sets, elements that are only in set b, not in a.

Example:

Input:
a = {1, 2, 3, 4, 5}
b = {6, 7, 8, 2, 3}
Output:
1 2 3 4 5 6 7 8
2 3
1 4 5
Your Task:
Your task is to complete the function all_in_set(), common_in_set() and diff() to perform union, intersection and difference between two sets and print the elements in the set after each operation.

Constraints:
1 <= S[i] <= 104
'''
#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3

# Function to find common elements in sets
# should return the intersection of sets
def common_in_set(a, b):
    # Your code here
    return a & b

# Function to find difference in sets
# Should return the difference in sets
def diff(a, b):
    # Your code here
    return a - b
    

# Function to find union of sets
# Should return the union of sets
def all_in_set(a, b):
    # Your code here
    
    return a | b

#{ 
#Driver Code Starts.

# Driver code
def main():
    testcase = int(input())
    
    # looping through all testcases
    while testcase > 0:
        
        # taking input of set
        a = {int(x) for x in input().split()}
        b = {int(x) for x in input().split()}
        
        for x in all_in_set(a, b):
            print (x, end = ' ')
            
        print ()
        
        for x in common_in_set(a, b):
            print (x, end = ' ')
            
        print ()
        
        for x in diff(a, b):
            print (x, end = ' ')
        
        print ()
        
        testcase -= 1

if __name__ == '__main__':
    main()
#} Driver Code Ends