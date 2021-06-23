'''
You are familiar with most of the properties of the dictionary in Python. Add some more info about dictionaries through dictionary formatting and deleting key-value pairs.

Formatting:

hash = {}
hash['Geeks'] = 5
hash['geeksforgeeks'] = 13
key = 'Geeks'
s = ("Count of characters is " + 
hash[key] + " in " + key)             
# results in: Count of characters is 
5 in Geeks.
Deleting:

dict = {'a' : 1, 'b': 2, 'c' : 3, 'd' : 4}
del dict['c']          
# delete entry for 'c'
Let's get this into the head by solving a question. Given a list of some students in a list and their corresponding marks in another list. The task is to do some operations as described below:
a. i key value: Iserts key and value in the dictionary, and print 'Inserted'.
b. d key: Delete the entry for a given key and print 'Deleted' if the key to be deleted is present, else print '-1'.
c. key: Print marks of a given key in a statement as "Marks of student name is : marks".

Example:

Input:
N = 5
i geeks 100
i for 200
d geeks
i geeks 300
p geeks
Output:
Inserted
Inserted
Deleted
Inserted
Marks of geeks is 300
Explanation:
For first four queries, insert and del 
operation happens, correspondingly Inserted 
And Deleted is printed. For the last query, 
marks of geeks is printed.
Your Task:
Your task is to complete the function insert_dict(), del_dict() and print_dict() which should perform the operations as required. If nothing is printed for a test case, print "-1".

Constraints:
1 <= N <= 104
1 <= marks <= 104
I/p -
5
i geeks 100
i for 200
d geeks
i geeks 300
p geeks
O/p -
Inserted
Inserted
Deleted
Inserted
Marks of geeks is 300
'''
#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3

# insert into dictionary
def insert_dict(query, dict):
    k = str(query[1])
    v = str(query[2])
    dict[k] = v

# deleting from dictionary
def del_dict(query, dict):
    
    key =  str(query[1])
    if key in dict.keys():
        dict.pop(key)
        return True
    else:
        return False
    
# print marks of required name
def print_dict(key, dict):
    
    if key in dict.keys():
        print('Marks of '+key+' is '+dict[key])
    else:
        return False
    
    
    

#{ 
#Driver Code Starts.
# Driver code
def main():
    # testcase input
    testcase = int(input())
    
    # looping through testcases
    while(testcase > 0):
        
        N = int(input())
        
        i = 0
        dict = {}
        while i < N:
            flag = False
            delete = False
            query = input().split()
            if(query[0] == 'i'):
                insert_dict(query, dict)
                print ("Inserted")
            
            if(query[0] == 'd'):
                if del_dict(query, dict) is False:
                    print ("-1")
                else:
                    print ("Deleted")
            
            if(query[0] == 'p'):
                if(print_dict(query[1], dict) is False):
                    print ("-1")
                    
            i+=1
            
        testcase -= 1


if __name__ == '__main__':
    main()
#} Driver Code Ends