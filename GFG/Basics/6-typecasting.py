'''
In Python, we use the input() function and put this function in either int(), float(), or bool() to typecast the input into required data type. Also, integers, floating-points and boolean variables don't have any range in Python. As long as you have enough memory, you can work with them.

In this question, you will take input of 4 variables that are in separate lines. The first variable is an integer, the second is a string(single/multiple words possible), the third is a floating number, the fourth is a boolean value.
You need to take the inputs and print the outputs

'''

def inPut():
    #Take input and assign the input to a, b, c, d. Please also typecast as type() will produce wrong answer without it
    a = int(input())  ## a is integer
    b = input() ## b is string
    c = float(input()) ## c is float
    d = bool(input()) ## d is a boolean
    
    print(a, type(a))
    print(b, type(b))
    print(c, type(c))
    print(d, type(d))
   
   

#{ 
#Driver Code Starts.

def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        inPut() #the function that gets things done
        testcases-=1
        


if __name__=='__main__':
    main()



#} Driver Code Ends