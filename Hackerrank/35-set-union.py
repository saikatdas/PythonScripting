"""
The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed to only French and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper. The same student could be in both sets. Your task is to find the total number of students who have subscribed to at least one newspaper.

Sample Input

9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
Sample Output

13
"""

if __name__ == '__main__':
    e = int(input())
    engInput = set(input().split())
    f = int(input())
    frenchInput = set(input().split())
    
    uCount = len(engInput.union(frenchInput))
    print(uCount)