'''
his module talks about dictionaries in Python. In Python, the efficient way to hash key/value pair is called a dictionary.

Initialization:

dict = {}
Setting values:

dict['a'] = 1 
dict['b'] = 2
Fetching values:

dict['a'] gives 1 as output 
dict['b'] gives 2 as output
Moving on to the question to implement a dictionary. Given a list of strings containing names of students and another list containing marks of corresponding students. The task is to create a dictionary to store marks of students with their names (name will be unique).

Example:

Input: 
N = 5 
names = [john, ala, ilia, sudan, mercy] 
marks = [100, 200, 150, 80, 300]
Output:
ala 200 
ilia 150 
john 100 
mercy 300 
sudan 80
Your Task:
The task is to complete the function create_dict() which takes arr as input and creates a dictionary then returns it.

Constraints:
1 <= N <= 104
1 <= marks <= 104
'''
#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3

# Function to create dictionary
# arr is list of tuple. tuple contain name and marks.

def create_dict(arr):
    
    return dict(arr)



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
        
        dict = create_dict(arr)
        
        for key in sorted(dict.keys()):
            print (key, dict[key])
        
        testcases -= 1
 
if __name__ == '__main__':
    main()
#} Driver Code Ends