# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
def createList(n):
    string = ''
    for i in range(1,n+1,1):
        string += f'{i}'
    return string

if __name__ == '__main__':
    c = 0
    n = int(input())
    string = input().split()
    k = int(input())
    nArr = createList(n)
    listArr = list(combinations(nArr,k))
    kArr = createList(k)
    
    for item in listArr:
            for kItem in kArr:
                if kItem in item:
                    c += 1
                    break
    
    ans = c / len(listArr)
    print(format(ans,".12f"))
