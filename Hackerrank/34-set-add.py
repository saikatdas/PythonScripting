# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of N country stamps.

Find the total number of distinct country stamps
 s = set('HackerRank')
s.add('H')
 print s
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
 print s.add('HackerRank')
None
print s
set(['a', 'c', 'e', 'HackerRank', 'H', 'k', 'n', 'r', 'R'])

Sample Input

7
UK
China
USA
France
New Zealand
UK
France 
Sample Output

5
"""
if __name__ == '__main__':
    country = set()
    n = int(input())
    for i in range(n):
        s = input()
        country.add(s)
    print(len(country))