'''
his module talks about Set in Python. A set is an unordered collection of items where every element is unique and must be immutable(fixed), but the set is mutable. You cannot access an element of the set using indexing or slicing, but you can update the set.

Some important functions in Set in Python:
add(): Adds an element to the set.
clear(): Removes all elements from the set
discard(): Removes an element from the set if present.
remove(): Removes an element from the set. If the element is not present, it raises an error.
pop(): Removes and returns an arbitrary set element. Raise the error if the set is empty.
union(): Returns the union of sets in a new set
update(): Updates the set with the union of itself and others
len(): Return the length of the set.
sorted(): Return a new sorted list from elements in the set.
sum(): Return the sum of all elements in the set.

Let's implement these methods through a question. Given Q queries to do some operation on Set, the task is to perform all the queries in the Set as given below:
a. i element: Adds an element to the set.
b. r element: Remove an element from the set.
c. s: Find the sum of elements in the set. Returns the sum of elements in the set.

Example:

Input:
Q = 4
S = {1, 2}
i 5
i 6
r 5
s
Output:
6
Explanation:
5 is added into the set
6 is added into the set
5 is removed from the set
So, now set is S = {1, 2, 6}
sum = 9
Your Task:

Your task is to complete the functions insert(), remove_from_set() and sum_set() that performs the specified tasks.

Constraints:
1 <= S[i] <= 104
I/P ->
4
6 7 81 2 1
i 3
i 4
r 6
s
'''

# no return should be there, and no print statement
def insert(S, element):
    S.add(element)
# Function to remove element from set
# No return and nothing to print
def remove_from_set(S, element):
    # Your code here
    
    S.remove(element)
# Function to find sum of elements in set
# return value should be there as sum
def sum_set(S):
    return sum(S)
# Driver Code
def main():
    
    # Testcase input
    testcase = int(input())
    
    # looping through testcases
    while testcase > 0:
        query = int(input())
        st = {int(x) for x in input().split()}
        
        while query > 0:
            
            q = input().split()
            
            if(q[0] == 'i'):
                element = int(q[1])
                insert(st, element)
                for i in st:
                    print (i, end=' ')
                print ()
                
            if(q[0] == 'r'):
                element = int(q[1])
                remove_from_set(st, element)
                for i in st:
                    print (i, end=' ')
                print ()
            
            if(q[0] == 's'):
                print (sum_set(st))
            
            query -= 1
            
        testcase -= 1

if __name__ == '__main__':
    main()
#} Driver Code Ends