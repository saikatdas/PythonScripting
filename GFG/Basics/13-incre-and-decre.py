'''
Given two numbers X and Y. Your task is to complete the function do_operation(), which print the value of X decremented by 1 and value of Y after incrementing it by 1.
'''
#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3

# Function to perform increment and decrement
def do_operation(X, Y):
    # Your code here
    X -= 1 
    Y += 1
    print (X)
    print (Y)

#{ 
#Driver Code Starts.


# Driver code
def main():
    testcase = int(input())
    
    while(testcase > 0):
        input1 = input().split()
        X = int(input1[0])
        Y = int(input1[1])
        do_operation(X, Y)
        testcase -= 1
        

if __name__ == '__main__':
    main()
#} Driver Code Ends