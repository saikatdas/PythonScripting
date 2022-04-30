"""
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
    
    for c in range(customer):

        shoeSize , price = map(int , input().split())

        if shoeSize in shoeStock:
            sum += price
            shoeStock[shoeSize] -=1
            # shoeStock.remove(shoeSize)
    print(sum)
    # shoeStockCounter = Counter(shoeStock).items() #LIST WITH TUPLE [(1,3), (2,4)]

    # noOfCustomer = int(input())
    # modifiedShoeStock = []
    # for i in range(noOfCustomer):
    #      a = input().split()
    #      size = int(a[0])
    #      price = int(a[1])

    #      if size in Counter(shoeStock).keys():

    #          for shoe in range(shoeStockCounter):
    #             y = list(shoe)



