"""
    You are given a set A and n other sets.
Your job is to find whether set A is a strict superset of each of the N sets.

Print True, if A is a strict superset of each of the  N sets. Otherwise, print False.

Sample Input 0

1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12
Sample Output 0

False

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    
    isStrictSuperSet = True
    setA = set(map(int , input().split())) 
    n = int(input())
    
    for _ in range(n):
        setInput = set(map(int , input().split()))
        if  not setA.issuperset(setInput):
            isStrictSuperSet = False
            break
    print(isStrictSuperSet)