if __name__ == "__main__":
    k = int(input())
    n = list(map(int , input().split()))
    
    n.sort()
    length = len(n)
    print(n[length - 1])
    