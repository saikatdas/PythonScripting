"""
    Sample Input

 16
 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
 4
 intersection_update 10
 2 3 5 6 8 9 1 4 7 11
 update 2
 55 66
 symmetric_difference_update 5
 22 7 35 62 58
 difference_update 7
 11 22 35 55 58 62 66

Sample Output

38

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())
    setA = set(map(int , input().split()))
    sum = 0
    m = int(input())
    
    for _ in range(m):
        operation_noOfElements = input().split()
        operation = operation_noOfElements[0]
        noOfElements = int(operation_noOfElements[1])

        setB = set(map(int , input().split()))

        if(operation == 'update'):
            setA.update(setB)
            
        elif(operation == 'intersection_update'):
            setA.intersection_update(setB)
            
        elif(operation == 'difference_update'):
            setA.difference_update(setB)

        elif(operation == 'symmetric_difference_update'):
            setA.symmetric_difference_update(setB)

    for e in setA:
        sum += e
    print(sum)
    
    