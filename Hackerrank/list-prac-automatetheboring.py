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

Tuples are like strings , immutable in nature
id(var) is same like &var

del(spam[0]) and spam.remove('cat')

use del statement when you know the list index for deleting item
use remove statement when you know the value of the element to be deleted.



Here's a little demonstration:

import copy

a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]
Using normal assignment operatings to copy:

d = c

print id(c) == id(d)          # True - d is the same object as c
print id(c[0]) == id(d[0])    # True - d[0] is the same object as c[0]
Using a shallow copy:

d = copy.copy(c)

print id(c) == id(d)          # False - d is now a new object
print id(c[0]) == id(d[0])    # True - d[0] is the same object as c[0]
Using a deep copy:

d = copy.deepcopy(c)

print id(c) == id(d)          # False - d is now a new object
print id(c[0]) == id(d[0])    # False - d[0] is now a new object


Variables will contain references to list values rather than list values themselves. But for strings and integer values, variables simply contain the string or integer value. Python uses references whenever variables must store values of mutable data types, such as lists or dictionaries. For values of immutable data types such as strings, integers, or tuples, Python variables will store the value itself.

Although Python variables technically contain references to list or dictionary values, people often casually say that the variable contains the list or dictionary.

Ex-1 from - https://automatetheboringstuff.com/2e/chapter4/
spam = ['apples', 'bananas', 'tofu', 'cats']
Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item.
For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'.
But your function should be able to work with any list value passed to it.
Be sure to test the case where an empty list [] is passed to your function

Sol -

if __name__ == '__main__':
    spam = ['apples', 'bananas', 'tofu', 'cats']
    if len(spam) != 0:
        spam.insert(len(spam)-1,'and')
        t = '\''+' '.join(spam)+'\''
        print(t)
Ex-2

Coin Flip Streaks
For this exercise, we’ll try doing an experiment.
If you flip a coin 100 times and write down an “H” for each heads and “T” for each tails, you’ll create a list that looks like “T T T T H H H H T T.”
If you ask a human to make up 100 random coin flips, you’ll probably end up with alternating head-tail results like “H T H T H H T H T T,” which looks random (to humans), but isn’t mathematically random.
A human will almost never write down a streak of six heads or six tails in a row, even though it is highly likely to happen in truly random coin flips. Humans are predictably bad at being random.

Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated list of heads and tails. Your program breaks up the experiment into two parts: the first part generates a list of randomly selected 'heads' and 'tails' values, and the second part checks if there is a streak in it.
Put all of this code in a loop that repeats the experiment 10,000 times so we can find out what percentage of the coin flips contains a streak of six heads or tails in a row. As a hint, the function call random.randint(0, 1) will return a 0 value 50% of the time and a 1 value the other 50% of the time.

You can start with the following template:

import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.

    # Code that checks if there is a streak of 6 heads or tails in a row.
print('Chance of streak: %s%%' % (numberOfStreaks / 100))

Of course, this is only an estimate, but 10,000 is a decent sample size. Some knowledge of mathematics could give you the exact answer and save you the trouble of writing a program, but programmers are notoriously bad at math.

"""





