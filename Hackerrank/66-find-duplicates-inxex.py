"""
Program to find duplicates and their associated index

I/P -
This is a a a tool is

O/ P -
----------
is
1 6
----------
----------
a
2 3 4
----------
"""
def printIndex(s,string):
    k = []
    for i in range(len(s)):
        if(s[i] == string):
            k.append(i)
    return k

if __name__ == '__main__':
    s = input().split()
    d = {}
    dupList = []
    #---------Add item in a Dictionary-------------------------------------------------------
    for e in s:
        if e in d:
            d[e] += 1
        else:
            d[e] = 1
    # {'This': 1, 'is': 1, 'a': 3, 'tool': 1}
    #----------------------------------------------------------------------------------------
    for k,v in d.items():
        if (d[k] > 1):
            dupList.append(k)
    # storing duplicate string from this dictionary to a List , how do I know it's duplicate ? If it appear more then 1 in a dictionary then there is duplicates in
    #dupList will contain duplicate values from the dictionary

    for v in dupList:
        k = printIndex(s , v)
        print('----------')
        print(v)
        print(*k)
        print('----------')
    # once you know the duplicate , you can loop through the list (or sentence) and print the index
