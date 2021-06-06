'''
Moving on, Lets introduce 3 more operators in python, is, is not & in.

'is' and 'is not' operators are coding equivalents of '==' and '!='  respectively. However, there are some minor differences that will be covered in the second module.

'in' operator is used to check if something is in some other thing, like 5 in range(2,6). It's useful in loops.

There is List (no need to know about it now, we would be covering it afterwards) of numbers num_list, and some integer queries Q. You need to tell if the numbers are present in the list or not, by returning True or False.

Example:

Input: 
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Q = [3, 6, 8, 12] 
Output: 
True 
True 
True
False
Explanation:
Since 3, 6, 8 are preset in the given
list and 12 is not present.
'''

#Function to find if number is present in the list or not
def number_present(num_list, Q):
    #num is a 'list', Q is a 'int'
    for i in range(len(num_list)):    #write this here - i in range(len(num_list))
                              # see the use of 'in' in for loop
        if (num_list[i] is Q): #write this here - num_list[i] is Q
                              # see the use of 'is' as equal to
            return True
    return False 

#{ 
#Driver Code Starts.
def main():
    testcases = int(input())
    while testcases :
        num_list = input()
        num_list = num_list.split()
        for i in range(len(num_list)):
            num_list[i] = int(num_list[i])
        
        q = input()
        q = q.split()
        for i in range(len(q)):
            q[i] = int(q[i])
            
        for i in range(len(q)):
            if number_present(num_list, q[i]):
                print("True")
            else:
                print("False")
        testcases-=1

if __name__ == '__main__' :
    main()
#} Driver Code Ends