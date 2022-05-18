"""
The defaultdict tool is a container in the collections class of Python. It's similar to the usual dictionary (dict) container, but the only difference is that a defaultdict will have a default value if that key has not been set yet. If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want.
For example:

from collections import defaultdict
d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print i
This prints:

('python', ['awesome', 'language'])
('something-else', ['not relevant'])
"""
from collections import defaultdict
n, m = list(map(int, input().split()))
grp = list()
d = defaultdict(list)

for i in range(n):
    d[input()].append(i+1)
   
for j in range(m):
    grp.append(input())
    
for item in grp:
    if (item in d):
        print(" ".join( map(str,d[item])))
    else:
        print ('-1')
