'''
Python provides us a special functionality to achieve this. We use the '*' operator to multiply a string by a positive integer 'x' to print it x number of times
'''

#User function Template for python3

# Function to print given string 'x' times
def print_fun(string, x):
    # Your code here
    
    
    print(string * x)

#{ 
#Driver Code Starts.

# Driver Code
def main():
    testcases = int(input())
    
    # Loop for testcases
    while(testcases > 0):
        string = input()
        x = int(input())
        print_fun(string, x)
        testcases -= 1

if __name__ == '__main__':
    main()
    
#} Driver Code Ends