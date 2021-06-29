'''
'''
def getMinMark(stuMark):
    stuMark.sort(key = lambda x: x[1])
    return stuMark
if __name__ == '__main__':
    stuList = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        myStu = []
        myStu.append(name)
        myStu.append(score)
        stuList.append(myStu)
    
    sortedByMark = getMinMark(stuList)
    secondMinMarkList = sortedByMark[1]
    print('2nd Min MarkList',secondMinMarkList)
    secondMinMark = secondMinMarkList[1]
    print('2nd Min Mark',secondMinMark)
    print(sortedByMark.sort(key=secondMinMark))
    
    
        
        