"""
Check if A is a subset of B.
Sample Input

3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2
Sample Output

True 
False
False    
"""

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        lenSet1 = int(input())
        setList1    = set(input().split())
            
        lenSet2 = int(input())
        setList2    = set(input().split())        
        print(setList1.issubset(setList2))