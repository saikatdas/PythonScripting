'''
Task

You are given a date. Your task is to find what the day is on that date.
nput Format

A single line of input containing the space separated month, day and year, respectively, in  MM DD YYYY  format.

Constraints

Output Format

Output the correct day in capital letters.

Sample Input

08 05 2015
Sample Output

WEDNESDAY
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

dt =input()

month,day,year = dt.split()
d = int(day)
m = int(month)
y = int(year)
val = calendar.weekday(y, m, d)

if (val == 0):
    print("MONDAY")
elif (val == 1):
    print("TUESDAY")
elif (val == 2):
    print("WEDNESDAY")
elif (val == 3):
    print("THURSDAY")
elif (val == 4):
    print("FRIDAY")
elif (val == 5):
    print("SATURDAY")
elif (val == 6):
    print("SUNDAY")


