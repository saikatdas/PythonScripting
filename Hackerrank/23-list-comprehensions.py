    """You are given three integers x,y,z and  representing the dimensions of a cuboid along with an integer n .
    Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n. Here, 0<=i<=x , 0<=i<=y , 0<=i<=z. Please use list comprehensions rather than multiple
    loops, as a learning exercise.
    """



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




