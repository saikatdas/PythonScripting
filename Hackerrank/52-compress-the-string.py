"""
groupby is very important
https://www.pythonpool.com/pythons-itertools-groupby/
"""
from itertools import groupby
for k,c in groupby(input()):
    print((len(list(c)),int(k)),end=' ')
