from itertools import combinations
if __name__ == '__main__':
    s = input().split()
    strInput = s[0]
    k = int(s[1])
   
    for i in range(1,k+1):
        x = list(combinations(strInput,i))
        print(*x)
