'''
You are given a string S.
Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
In the second line, print True if S has any alphabetical characters. Otherwise, print False.
In the third line, print True if S has any digits. Otherwise, print False.
In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
In the fifth line, print True if S has any uppercase characters. Otherwise, print False.
Sample Input

qA2
Sample Output

True
True
True
True
True

'''
def printRes(s,func):
    
    i = 0
    res = 'False'
    for i in range(len(s)):
        
        if (func == 'alnum'):
            
            if s[i].isalnum():
                res = 'True'
                break
        if (func == 'alpha'):
            if s[i].isalpha():
                res = 'True'
                break
            
        if (func == 'digit'):
            
            if (s[i].isdigit()):
                res = 'True'
                break
            
        if (func == 'low'):
            if (s[i].islower()):
                res = 'True'
                break
            
        if (func == 'upper'):
            
            if (s[i].isupper()):
                res = 'True'
                break
        
    print(res)
    
        
      

if __name__ == '__main__':
    
    s = input()    
    printRes(s,'alnum')
    printRes(s,'alpha')
    printRes(s,'digit')
    printRes(s,'low')
    printRes(s,'upper')
    
    