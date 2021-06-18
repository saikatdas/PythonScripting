'''
As you would already know, Modules refer to files containing already compiled Python statements and definitions. This allow us to break down large number of code lines into group of manageable files.
Lets play by importing some modules in our code.

You are required to print values of pi constant and e constant using math library.

Output:

pi = 3.141592653589793 
e = 2.718281828459045
Your Task:
This is a function problem. You don't need to take any input. just Complete math_func().
'''
#User function Template for python3
import math

def math_func():
    #import math module and print pi and e
    print("pi =",math.pi)
    print("e =",math.e)
    

#{ 
#Driver Code Starts.

def main():
    math_func()
    
    
if __name__ == '__main__':
    main()
#} Driver Code Ends