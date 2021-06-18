
'''
Naive method to find a prime number in python (bad approch)
'''
def isPrime(n):
    i = 1
    count = 0
    if n == 0 or n == 1:
        return False
    
    for i in range(i, n+1,1):
        # print("i",i)
        if n % i == 0:
            count += 1
    
    # print("count now -",count)
    if(count == 2):
        return True
    else:
        return False



def main():
    print('no of TestCase ?')
    t = int(input())
    while( t > 0):
        n = int(input())
        print(isPrime(n))
        t -= 1



if __name__=='__main__':
    main()

