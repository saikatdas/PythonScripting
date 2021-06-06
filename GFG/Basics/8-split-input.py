'''
Example:
Input:
string = Geeks 2 2.3445

Output:
Geeks 4.3445
Your Task:
Your task is to complete the function inPutS(), In this function, you will take input a single line string comprised of string, int, and float. You'll split the string and assign string to s, int to i, and float to f. Print a final string comprised of s and (i + f).
'''
#User function Template for python3

def inPutS():
    string = input().split() ## input in a single line()
    s, i , f = string ## split the a into three parts: string, integer, and f. 
    
    n = str (int(i) + float(f))
    print(s + " " + n) ##type cast i to int, f to float. Add i with f. Typecast the result to string

#{ 
#  Driver Code Starts

def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        inPutS() #the function that gets things done
        testcases-=1
        


if __name__=='__main__':
    main()
# } Driver Code Ends