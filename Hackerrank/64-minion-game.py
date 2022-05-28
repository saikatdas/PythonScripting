"""
For the word "BANANA", the first vowel 'A' occurs at position 1, len("BANANA") = 6, so there are 6-1 = 5 substrings starting with this letter 'A': ['A', 'AN', 'ANA', 'ANAN', 'ANANA'], you add one extra letter to that specific letter 'A' until you get to the end of the word.
"""

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
