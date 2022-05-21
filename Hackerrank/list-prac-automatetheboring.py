"""
automate th boring stuff 
del stuList[2] will delete the 2nd element of the list

The del statement can also be used on a simple variable to delete it, as if it were an “unassignment” statement.
If you try to use the variable after deleting it, you will get a NameError error because the variable no longer exists. In practice, you almost never need to delete simple variables.
The del statement is mostly used to delete values from lists.


List in and not in operators

List len(lis) will return the length of the list



enumerate - instead of range(len(someList))

>>> supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
>>> for index, item in enumerate(supplies):
...     print('Index ' + str(index) + ' in supplies is: ' + item)

Index 0 in supplies is: pens
Index 1 in supplies is: staplers


The enumerate() function is useful if you need both the item and the item’s index in the loop’s block.

l =['a', 'b', 'c']
for k,v in enumerate(l):
    print('Index ' + str(k) + ' in l is ' +  str(v))

l = ['a', 'b', 'c']
list.index('b')
list.insert(index,'fhgfg') where index is 0,1,2,3,4



Methods belong to a single data type. The append() and insert() methods are list methods and can be called only on list values, not on other values such as strings or integers. Enter the following into the interactive shell, and note the AttributeError error messages that show up:

>>> eggs = 'hello'
>>> eggs.append('world')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    eggs.append('world')
AttributeError: 'str' object has no attribute 'append'
>>> bacon = 42
>>> bacon.insert(1, 'world')
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    bacon.insert(1, 'world')
AttributeError: 'int' object has no attribute 'insert'


l = ['a', 'b', 'c']
l.remove('a')
l.sort()
l.reverse()

But lists and strings are different in an important way. A list value is a mutable data type: it can have values added, removed, or changed. However, a string is immutable: it cannot be changed. Trying to reassign a single character in a string results in a TypeError error, as you can see by entering the following into the interactive shell:

"""
