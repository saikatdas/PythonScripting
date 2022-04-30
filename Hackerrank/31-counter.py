"""
    Counter is a subclass of dict that’s specially designed for counting hashable objects in Python. It’s a dictionary that stores objects as keys and counts as values. To count with Counter, you typically provide a sequence or iterable of hashable objects as an argument to the class’s constructor.

    ßCounter internally iterates through the input sequence, counts the number of times a given object occurs, and stores objects as keys and the counts as values. In the next section, you’ll learn about different ways to construct counters.

    Ex - Counter("mississippi")
    Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})

    myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
     print Counter(myList)
    Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})

    print Counter(myList).items()
    [(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]

     print Counter(myList).keys()
    [1, 2, 3, 4, 5]

    print Counter(myList).values()
    [3, 4, 4, 2, 1]

    Without the counter function


if __name__ == '__main__':
    sum = 0
    n = int(input())
    shoeStock = list(map(int , input().split()))

    customer = int(input())

    for c in range(customer):
        a = input().split()
        shoeSize = int(a[0])
        price = int(a[1])

        if shoeSize in shoeStock:
            sum += price
            shoeStock.remove(shoeSize)
    print(sum)

Sample Input

10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
Sample Output

200
Explanation

Customer 1: Purchased size 6 shoe for $55.
Customer 2: Purchased size 6 shoe for $45.
Customer 3: Size 6 no longer available, so no purchase.
Customer 4: Purchased size 4 shoe for $40.
Customer 5: Purchased size 18 shoe for $60.
Customer 6: Size 10 not available, so no purchase.
Total = 200

"""

from collections import Counter
if __name__ == '__main__':
    sum = 0
    n = int(input())
    shoeStock = list(map(int , input().split()))
    
    customer = int(input())
    
    shoeStockCounter = Counter(shoeStock) #LIST WITH TUPLE [(1,3), (2,4)]

    for i in range(customer):

        size , price = map(int , input().split())

        if shoeStockCounter[size]:
             sum += price
             shoeStockCounter[size] -= 1
    print(sum)




