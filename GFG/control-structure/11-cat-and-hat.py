'''
ou are given a string str, you need to print True if cat and hat appear same number of times in str, otherwise print False.

Note: str contains only lowercase characters.

Hint: You may use len(str) to get length of string. Also, you can obtain a certain part of the string using string slicing- str[startindex:endindex]

Example 1:

Input:
str = catinahat
Output:
True
Explanation:
cat and hat both are present
1 number of times.
Example 2:

Input:
str = bazingaa
Output:
True
Explanation:
cat and hat both are present
0 number of times.
'''

#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3

def cat_hat(str):
  cat = 0
  hat = 0
  i = 0
  j = 0
  for i in range(i,(len(str)-1),1):
      if 'c' == str[i]:
          if ( (i + 2) <=  (len(str)-1)):
              
              if 'a' == str[i+1]:
                  
                  if 't' == str[i+2]:
                      cat += 1
                      i += 3
                  
  for j in range(j,(len(str)-1),1):
      if 'h' == str[j]:
          if ( (j + 2) <=  (len(str)-1)):
              
              if 'a' == str[j+1]:
                  
                  if 't' == str[j+2]:
                    
                    hat += 1
                    j += 3
    
#   print(cat,hat)
  if ( cat == hat ):
      return True
    
  else:
      return False
        
   


#{ 
#Driver Code Starts.




def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        str = input()
        print(cat_hat(str))
        testcases-=1
        


if __name__=='__main__':
    main()
#} Driver Code Ends