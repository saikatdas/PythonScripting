  """
        for element in re:
            print(''.join(element))

    """

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
if __name__ == '__main__':
    strInput = input().split()  #can also be written as a,b = input().split()
    re = list(permutations(strInput[0] , int(strInput[1])))
    re.sort()

[print(''.join(e)) for e in re]


    