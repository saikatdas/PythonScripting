'''
Python has a lot of string methods that can be used to manipulate the strings like converting to lowercase, capitalizing, trimming the spaces and so on.

In this question, we'll take a look at inbuilt string methods like title(), swapcase(), find(), strip().
You'll be given a string str and x, you'll perform various operations on them.

Example:

Input:
str = hello 
x = llo
Output:
hello 
2 
Hello 
HELLO
Ref - https://www.w3schools.com/python/python_ref_string.asp
'''
#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3


def trim(str):
    return str.strip()     

def exists(str, x):
    return str.find(x)     

def titleIt(str):
    return  str.title()    

def casesSwap(str):
    return  str.swapcase()    


#{ 
#Driver Code Starts.

def main():
    testcases = int(input()) #testcases
    while(testcases>0):
        str = input()
        x = input()
        str = trim(str)
        print(str)
        print(exists(str, x))
        print(titleIt(str))
        print(casesSwap(str))
        testcases -= 1
        


if __name__=='__main__':
    main()
#} Driver Code Ends