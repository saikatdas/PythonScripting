    """
        Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i .
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands
where each command will be of the 7
types listed above. Iterate through each command in order
and perform the corresponding operation on your list.

Sample I/O -

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

O/P -

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
list.sort(key=lambda s: s.name, reverse=True)
"""
if __name__ == '__main__':
    N = int(input())
    arr = []
    i = 0
    for i in range(N):
        inputLine = input().split()
        if (inputLine[0] == 'insert'):
            #do insert
            arr.insert(int(inputLine[1]),int(inputLine[2]))

        elif (inputLine[0] == 'print'):
            #do print
            print(arr)

        elif (inputLine[0] == 'remove'):
            #do remove
            arr.remove(inputLine[1])

        elif (inputLine[0] == 'append'):
            #do append
            arr.append(inputLine[1])

        elif (inputLine[0] == 'sort'):
            #do sort
            arr.sort()
        elif (inputLine[0] == 'pop') :
            #do pop
            arr.pop()
        elif (inputLine[0] == 'reverse') :
            #do reverse
            arr.reverse()
        else :
            print('wrong operation')
            
        
