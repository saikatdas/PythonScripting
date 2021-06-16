'''
Given two strings a and b. The task is to make a new string where the string with longer length should be in between and the one with shorter length should be outside on front and end. New string should be like shorter+longer+shorter.

Example:

Input: 
a = Hi, b = There
Output: 
HiThereHi
Explanation: 
After joining short+long+short strings, 
we have new string as "HiThereHi".
Your Task:

Your task is to complete the function combo_string(), which joins short+long+short strings and returns the new concatenated string..

Constraints:
1 <= |a, b| <= 103
'''
#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3

# Function to join given strings
def combo_string(a, b):
  
  # your code here
  len_a = int(len(a))
  len_b = int(len(b))
  short = ""
  longer = ""
  if len_a > len_b:
      #a is longer
      longer = a
      short = b
  else:
      longer = b
      short = a
      
      
  
  return short+longer+short

#{ 
#Driver Code Starts.
# Driver Code
def main():
    # 
    testcases = int(input())
    
    while(testcases > 0):
        string = input().split()
        string1 = string[0]
        string2 = string[1]
        
        testcases -= 1
        
        print (combo_string(string1, string2))

if __name__ == '__main__':
    main()
#} Driver Code Ends