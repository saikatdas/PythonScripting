'''
Given a positive integer x. Your task is to check, if it is even or odd (Any number that gives zero as remainder when divided by 2 is an even number)

Example 1:

Input:
x = 4
Output:
Even
Example 2:

Input:
x = 5
Output:
Odd
Your Task:

Your task is to complete the function checkEvenOdd(), which returns True (In python, True starts with caps T) if the number is even, else return False (In Python, False starts with caps F)
'''
#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3

def checkOddEven(x):
    if(x % 2 == 0):
      return True
    else:
        return False

#{ 
#Driver Code Starts.

# Driver Code
def main():
    
    # Testcase input
    testcases = int(input())
    
    # Looping through testcases
    while(testcases > 0):
        x = int(input())
        
        if(checkOddEven(x)):
            print ("Even")
        else:
            print ("Odd")
        
        
        testcases -= 1
 
if __name__ == '__main__':
    main()
#} Driver Code Ends