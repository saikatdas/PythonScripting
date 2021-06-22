'''
It's time to dive deeper into the dictionary in Python. How can you use a dictionary to store the frequency of elements in list L. Given below is one method:

for i in L:
     dict[i] = 0

for i in L:
     dict[i] += 1
Now, use this concept to solve a question. Given a list arr, of N positive integers, and a sum. The task is to check if any pair exists in the array whose sum is present in the array.

Example:

Input: 
N = 7 
sum = 8 
arr = [1, 2, 3, 3, 5, 5, 5] 
Output: 
Yes
Explanation:
Pair with sum 8 is present in
the array which is (5, 3).
Your Task:
Your task is to complete the function pair_sum() which returns True if the required pair is present, else return False. driver code will take care of the printing.

Constraints:
1 <= N, sum <= 104
1 <= arr[i] <= 104
'''
#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3

# Function to check if pair 
# with given sum exists
'''
For Input:
5
8
1 2 3 3 5 5 5
your output is: 
{1: 1, 2: 1, 3: 2, 5: 3
'''
import itertools

def findsubsets(s, n):
	return list(itertools.combinations(s, n))
	
def pair_sum(dict, N, arr, sum):
    mySet= set()
    
    for k,v in dict.items():
        mySet.add(k)

        listSub = findsubsets(mySet,2)

        for l in listSub:
            if( sum == l[0] +l[1]):
                return True

    return False


    

#{ 
#Driver Code Starts.
# Driver code
def main():
    
    # testcase input
    testcase = int(input())
    
    # looping through testcases
    while(testcase > 0):
        
        N = int(input())
        sum = int(input())
        dict = {}
        x = N
        arr = [int(i) for i in (input().split())]
        
        for i in arr:
            dict[i] = 0
                
        for i in arr:
            dict[i] +=1
    
        if pair_sum(dict, N, arr, sum) is True:
            print ("Yes")
        else:
            print ("No")
        
        testcase -= 1


if __name__ == '__main__':
    main()
#} Driver Code Ends