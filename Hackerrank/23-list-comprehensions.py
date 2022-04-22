
def createList(x):
    xList = []
    for i in range(x+1):
        xList.append(i)
    return xList

def createResultList(allPermutationList,n):
    resultList = []
    for e in allPermutationList:
        sum = 0
        for element in e:
            sum += element
        if(sum != n):
            resultList.append(e)
    return resultList

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    #print([[i,j,k] for i in [0, 1, 2] for j in [0, 1, 2 ] for k in [0, 1, 2]])
    allPermutationList = [[i,j,k] for i in createList(x) for j in createList(y) for k in createList(z)]
    print(createResultList(allPermutationList,n))




