'''

Tuples are data structures that look a lot like lists. Unlike lists, tuples are immutable (meaning that they cannot be modified once created). This restricts their use because we cannot add, remove, or assign values; however, it gives us an advantage in space and time complexities.

A common tuple use is the swapping of 2 numbers:

a, b = b, a
Here a,b is a tuple, and it assigns itself the values of b,a .

Another awesome use of tuples is as keys in a dictionary. In other words, tuples are hashable.

Input Format

The first line contains an integer n , , denoting the number of elements in the tuple.
The second line contains n space-separated integers describing the elements in tuple t.

Output Format

Print the result of hash(t).
Sample Input 0

2
1 2
Sample Output 0

3713081631934410656
'''
if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(int(i) for i in input().split())
    print(hash(integer_list))
