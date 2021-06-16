'''
Regular expressions are extremely helpful in extracting useful information from loads of text. Regular expressions work on pattern-matching techniques. Extracting phone-number, validating passwords, and extracting images from web-pages are but a few examples of regex usage.

In this question, we'll learn the use of Regex in Python. You will be provided a string str in which you have to find all the numbers and print them.

Note: In Python, you need to import re module to use regex

Example:

Input: 
str = asdasd123asmdasdk34234kfdsd34sdfk5
Output: 
123 34234 34 5

Regex tutorial link - https://www.w3schools.com/python/python_regex.asp
'''
#{ 
#Driver Code Starts
#Initial Template for Python 3


import re ##import re module to use regex

 # } Driver Code Ends
#User function Template for python3



def numberMatcher(str):
    pat="[0-9]+"
    match=re.findall(pat,str) 
    if(match): 
        for i in match:
            print(i, end=" ")
    else:
        print(-1,end="")


#{ 
#Driver Code Starts.

def main():
    testcases = int(input()) #testcases
    while(testcases > 0):
        str = input()
        numberMatcher(str)
        print()
        testcases -= 1
        


if __name__=='__main__':
    main()
#} Driver Code Ends