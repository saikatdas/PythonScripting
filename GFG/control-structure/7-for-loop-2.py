'''
You are given a string str, you need to print its characters at even indices(index starts at 0).

Note: Please go through the range function to understand how to jump 2 steps.

Example 1:

Input:
str = DoctorPhenomenal
Output:
DcoPeoea
'''
#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3


def stringJumper(str):
    for i in range(0,len(str),2): ## from 0 to length of str and skip 2
        print(str[i], end="") ##printing character and separating characters by nothing



#{ 
#Driver Code Starts.



def main():
    testcases = int(input()) #testcases
    while(testcases>0):
        str = (input())
        stringJumper(str)
        print()##separating testcases outputs by newlines
        testcases -= 1
        


if __name__=='__main__':
    main()
#} Driver Code Ends