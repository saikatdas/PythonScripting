'''
In String Functions - I, you learnt some inbuilt functions of strings in Python. Now, let's take a look at some more functions.

a. S.lower(), S.upper(): returns the lowercase or uppercase version of the string.
b. S.startswith('string2'), S.endswith('string2'): tests if string starts or ends with the given string2.

Let us implement these through a question. Given a string S, the task is to check if this string starts and ends with gfg (case insensitive).

Example 1:

Input: 
S = gFgabcdEGfG
Output: 
Yes
Explanation: 
String starts and ends with gfg,
so output is Yes.
'''
#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3

# Function to check if string 
# starts and ends with 'gfg'
def gfg(S):
    b = S.lower()
    if( b.startswith('gfg') and b.endswith('gfg') ):  
        print ("Yes")
    else:
        print ("No")

#{ 
#Driver Code Starts.
# Driver Code
def main():
    # testcase input
    testcases = int(input())
    
    # looping through testcases
    while(testcases > 0):
        S = input()
        
        testcases -= 1
        
        gfg(S)

if __name__ == '__main__':
    main()
#} Driver Code Ends