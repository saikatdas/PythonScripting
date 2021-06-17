'''
e'll use Regex to validate a password. You will be provided a string str which you have to validate.

The validation rules are as follows:

The string is valid only if it starts with lowercase characters, followed by special characters !@#$% followed by numbers.
In any other case the string is not valid.
Example:

Input: 
str = asdsab@!@234
Output: 
True
Explanation: 
The string is valid as characters are
followed by special case characters 
which are then followed by numbers.
Your Task:

This is a function problem. Do not take any input. Complete the function validate() that takes str as input and returns True/False.
Regex Validator - https://regexr.com/
'''
#{ 
#Driver Code Starts
#Initial Template for Python 3






import re

 # } Driver Code Ends
#User function Template for python3

def validate(str):
    pat= "([a-z])+[!@#$%]+\d"
    match = re.search(pat, str)
    if(match):
        return True
    else:
        return False



#{ 
#Driver Code Starts.

def main():
    testcases = int(input()) #testcases
    while(testcases > 0):
        str = input()
        print(validate(str))
        testcases -= 1
        


if __name__=='__main__':
    main()
#} Driver Code Ends