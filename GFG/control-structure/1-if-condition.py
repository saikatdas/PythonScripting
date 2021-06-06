'''
 any conditional statement ends with ':' (proper indentation must be followed while working through loops).

There are two friends, John and Smith, and the parameters j_angry and s_angry to indicate if each is angry. You are in trouble if both of them are angry or no one of them is angry.
'''
#{ 
#Driver Code Starts
#Initial Template for Python 3



 # } Driver Code Ends

def friends_in_trouble(j_angry, s_angry):
    
    if((j_angry is s_angry)):
        
        return True
    return False

#{ 
#Driver Code Starts.

# Driver code    
def main():
    testcase = int(input())
    
    # loop for testcases
    while(testcase > 0):
        string = input().split()
        j_angry = string[0]
        s_angry = string[1]
        if(j_angry == 'True'):
            j_angry = True
        else:
            j_angry = False
        
        if(s_angry == 'True'):
            s_angry = True
        else:
            s_angry = False
            
        print(friends_in_trouble(j_angry, s_angry))
        
        testcase -= 1
    
if __name__ == '__main__':
    main()