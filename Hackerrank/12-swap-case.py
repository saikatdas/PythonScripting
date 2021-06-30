'''
swap case of a str.
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

Sample Input 0
HackerRank.com presents "Pythonist 2".

Sample Output 0
hACKERrANK.COM PRESENTS "pYTHONIST 2".
'''
def swap_case(s):
    newStr = ''
    for i in s:
        if(i.isupper()):
            newStr += i.lower()
        elif(i.islower()):
            newStr += i.upper()
        else:
            newStr +=i 
    return newStr

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)