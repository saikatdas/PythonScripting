"""
Math trick pattern print will not work if n<=14
1
22
333
.......
"""
for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print((10**(i)//9)*i)
