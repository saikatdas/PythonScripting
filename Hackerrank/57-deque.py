# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
read docs - https://docs.python.org/3/library/collections.html#collections.deque
Task

Perform append, pop, popleft and appendleft methods on an empty deque d.
"""
from collections import deque
if __name__ == '__main__':
    d = deque()
    n = int(input())
    for _ in range(n):
        c = input().split()
        if(c[0] == 'pop'):
            d.pop()
        elif(c[0] == 'append'):
            d.append(c[1])
        elif(c[0] == 'popleft'):
            d.popleft()
        elif(c[0] == 'appendleft'):
            d.appendleft(c[1])
    
    print(*d)
            