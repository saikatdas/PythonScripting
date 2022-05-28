def minion_game(string):
    # your code goes here
    s = string
    v = 'AEIOU'
    stuCount =0
    kCount = 0
    for i in range(len(s)):
        if(s[i] not in v):
            stuCount += (len(s) - i)
        else:
            kCount += (len(s) - i)
    if(stuCount > kCount):
        print('Stuart',stuCount)
    elif(stuCount < kCount):
        print('Kevin',kCount)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)
