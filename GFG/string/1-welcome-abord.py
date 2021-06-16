# strings are immutable and can not be changed
'''
This module talks about Strings in Python. String in Python is immutable (cannot be edited). You have learnt about separators in Python. Let's start String with first question given below:

Given name of a person, the task is to welcome the person by printing the name with "Welcome". If name is "John", you should print "Welcome John".

'''

#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3

# Function to Welcome the person
def welcomeAboard(name):
    print ("Welcome",name) # Your code here
   

#{ 
#Driver Code Starts.
# Driver Code
def main():
    
    # Testcase input
    testcases = int(input())
    
    # Looping through testcases
    while(testcases > 0):
        name = input()
        
        welcomeAboard(name);
        
        testcases -= 1
 
if __name__ == '__main__':
    main()
#} Driver Code Ends