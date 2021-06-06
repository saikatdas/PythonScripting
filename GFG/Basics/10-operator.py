'''
Your are familiar with input, output and data types in Python. Let us move on to play with operators in Python. Operators used widely in Python are '+',  '-', '*', '/', '**', '//'.


Arithmetic Operations:
a. Add ("+"): Adding X and Y.
b. Subtract ("-"): Subtracting X and Y.
c. Multiply ("*"): Multiply X and Y.
d. Divide ("/"): Divide X by Y.
e. Multiplying X, Y times ("**"): X raised to power Y.
f. Divide and floor the result ("//"): Divide and result is in integer form

'''
#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3

# Function to perform mathematical operation on X and Y
def do_operation(X, Y):
    # Your code here
    a = int(X) 
    b = int(Y)
    
    l = a + b
    m = a - b
    n = a * b
    o = a / b
    p = a ** b
    q = a // b
    print(l)
    print(m)
    print(n)
    print(o)
    print(p)
    print(q)

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
    