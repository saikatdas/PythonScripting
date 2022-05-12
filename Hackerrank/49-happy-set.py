"""
Input Format

The first line contains integers n and m separated by a space.
The second line contains n integers, the elements of the array.
The third and fourth lines contain m integers, A and B, respectively.

Output Format

Output a single integer, your total happiness.

Sample Input

3 2
1 5 3
3 1
5 7
Sample Output

1
"""

if __name__ == '__main__':
    h = 0
    n, m = list(map(int , input().split()))
    intList = list(map(int , input().split()))
    setA = set(map(int , input().split()))
    setB = set(map(int , input().split()))
    
    for e in intList:
        if e in setA:
            h+=1
        elif e in setB:
            h-=1
    print(h)
