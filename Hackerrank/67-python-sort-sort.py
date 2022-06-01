"""
https://www.hackerrank.com/challenges/python-sort-sort/problem?isFullScreen=true

Naive approch
"""

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []
    dictArr = {}
    tArr = {}
    resList = []
    i =0
    p = 0
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
        dictArr[i] = arr[i]
        i = i + 1

    k = int(input())
    for ke,v in dictArr.items():
        tArr[ke] = v[k]
    # sort_orders = sorted(orders.items(), key=lambda x: x[1], reverse=True)
    sortDictArr = sorted(tArr.items(), key=lambda x:x[1])

    for i in sortDictArr:
        resList.append(i[0])

    for k,v in dictArr.items():
        print(*dictArr[resList[p]])
        p += 1
