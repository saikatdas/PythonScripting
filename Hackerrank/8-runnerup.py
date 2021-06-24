'''
Find the runner up code
Sample Input 0

5
2 3 6 6 5
Sample Output 0

5
Explanation 0

Given list is [2 3 6 6 5]. The maximum score is 6, second maximum is5 . Hence, we print 5 as the runner-up score.
'''
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    mylist = sorted(arr)
    mylist.sort(reverse=True)
    max=mylist[0]
    result=max
    for i in mylist:
        if(max>i):
           result = i
           break
    print(result)
