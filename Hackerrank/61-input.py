# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
def cal(p,t):
    a = p.replace('x',str(t))
    c = a.replace('**',',')
    if (len(c) > 1):
        d = math.pow(int(c[0]),int(c[2]))
        return int(d)
    return int(c)
if __name__ == '__main__':
    s = 0
    sum_ = 0
    x,y = map(int,input().split())
    eq = input().split(' ')
    for item in range(0,len(eq),1):

        s = cal(eq[item],x)


    if (sum_ == y):
        print(sum_,True)
    else:
        print(sum_,False)
        