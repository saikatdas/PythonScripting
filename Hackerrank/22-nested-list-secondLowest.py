

if __name__ == '__main__':
    
    record = []
    stuName = []
    stuScore = []
    studentList = []
    dupRecord = []
    finalNameList = []
    n = int(input())
    i = 0
    for _ in range(n):
        name = input()
        score = float(input())
        studentList = []
        dupstudentList = []
        if (score not in stuScore):
            stuScore.insert(i,score)
            studentList.insert(i,name)
            studentList.insert(i,score)
            record.append(studentList)

        dupstudentList.insert(i,name)
        dupstudentList.insert(i,score)
        dupRecord.append(dupstudentList)
record.sort()
# print(record)
if ( n ==1 ):
    print(record[0][1])
else:
    # print(record[1][0])
    # print('duRecord print')
    # print(dupRecord)
    x = record[1][0]
    for i in dupRecord:
        if (x in i):
            finalNameList.append(i[1])
    finalNameList.sort()
    for name in finalNameList:
        print(name)




