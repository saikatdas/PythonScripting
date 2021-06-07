'''
Given two integer variables a and b, and a flag which is boolean. The task is to check the status and return accordingly.
Return "True" if either a or b (one of them) is positive. Except if the flag is True, then return True only if both of the variables a and b are negative.

Example: 

Input:
a = 1
b = -1
flag = False
Output:
True
Explanation:
Since a and b are positive and 
negative respectively and flag
is False, so return True.
'''
#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3

# Function to check value and 
# return accordingly
def check_status(a, b, flag):
    if ( flag ):
        if ( a < 0 and b < 0 ):
            return True
        
    else:
        if ( a > 0 and b > 0 ):
            return False
        
        
        if ( a > 0 or b > 0 ):
            return True
            
    return False    
    ##Your code here
    ##Either True or False is returned

#{ 
#Driver Code Starts.

# Driver Code
def main():
    
    # Testcase input
    testcases = int(input())
    
    # Looping through testcases
    while(testcases > 0):
        a = int(input())
        b = int(input())
        flag = input()
        
        if(flag == "True"):
            flag = True
        else:
            flag = False
        
        if(check_status(a, b, flag) is True):
            print ("True")
        else:
            print ("False")
        
        testcases -= 1
 
if __name__ == '__main__':
    main()
#} Driver Code Ends