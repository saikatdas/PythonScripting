'''
Output Format

Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input

ABCDCDC
CDC
Sample Output

2
Note - ths program can be simplified and optimized
'''
def count_substring(string, sub_string):
    lSub = len(sub_string)
    x = 0
    count = 0
    for i in range(x,len(string)):
        subStr = string[i:lSub + i]
        if subStr == sub_string:
            count += 1
        x += lSub
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)