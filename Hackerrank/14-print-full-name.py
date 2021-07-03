'''
Given first name , last name print it

Constraints

The length of the first and last names are each ≤10 .

Sample Input 0

Ross
Taylor
Sample Output 0

Hello Ross Taylor! You just delved into python.
Explanation 0

The input read by the program is stored as a string data type. A string is a collection of characters.
'''
def print_full_name(first, last):
    # Write your code here
    print('Hello '+first+' '+last+'! '+'You just delved into python.')
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)