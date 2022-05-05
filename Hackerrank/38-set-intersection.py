"""
intersection()
The .intersection() operator returns the intersection of a set and the set of elements in an iterable.
Sometimes, the & operator is used in place of the .intersection() operator, but it only operates on the set of elements in set.
The set is immutable to the .intersection() operation (or & operation).

  s = set("Hacker")
  print s.intersection("Rank")
set(['a', 'k'])

  print s.intersection(set(['R', 'a', 'n', 'k']))
set(['a', 'k'])

  print s.intersection(['R', 'a', 'n', 'k'])
set(['a', 'k'])

  print s.intersection(enumerate(['R', 'a', 'n', 'k']))
set([])

  print s.intersection({"Rank":1})
set([])

  s & set("Rank")
set(['a', 'k'])
Task
The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed only to French, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to both newspapers.

Sample Input

9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
Sample Output

5

"""


# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    engNumber = int(input())
    engSet = set(map(int , input().split()))
    
    frenchNumber = int(input())
    frenchSet = set(map(int , input().split()))
    
    print(len(engSet.intersection(frenchSet)))