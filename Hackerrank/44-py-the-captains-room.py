"""
Input Format

The first line consists of an integer,k, the size of each group.
The second line contains the unordered elements of the room number list.


Constraints
1 < k < 1000

Output Format

Output the Captain's room number.

Sample Input

5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2
Sample Output

8

"""

if __name__ == "__main__":
    k = int(input())
    n = list(map(int , input().split()))
    
    a = set()
    b = set()

    for element in n:
        if element not in a:
            a.add(element)
        else:
            b.add(element)

    print(*a.difference(b))
