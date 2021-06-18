'''
we'll implement class and create objects.

Examples:

Input:
Object1=> Name = Spiderman 
hp = 76 
boost = 4 
Object2=> Name = Hulk 
hp = 213 
boost = 1
Output: 
Spidlk 517
Explanation:
Object1=> Name = Spiderman, Hp = 76 * 4 
Object2=> Name = Hulk, Hp = 213 * 1 
length(Spiderman) / 2 = 4
4 characters = Spid 
length(Hulk) / 2 = 2
2 characters from end = lk 
Object3=> Name = Spid + lk 
Hp = 76 * 4 + 213 * 1 = 517
Your Task:
This is a function problem. You don't need to take any input. Complete the class functions getName() and getHp(); and also complete the function fusion(). The fusion function takes two objects and returns a third object that has following properties.
Name = first_half of obj1 Name + last_half of obj2 Name.
hp = hp of obj1 + hp of obj2

Constraints:

1 <= |Name| <=500
1 <= hp of obj1 <= 500
1 <= boost of obj1 <= 200
1 <= hp of obj2 <= 500
1 <= boost of obj2 <= 200
'''
#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3

class Character:
    def __init__(self, Name, hp):
        self.name = Name ##Assigning name to the current object's name variable
        self.hp = hp ##Assigning hp to the current object's hp variable
    def boost(self, boost):
        self.hp = self.hp * boost ## boosting current object's hp
    def getName(self):
        return self.name
        ##complete this. Return name of the current object
    def getHp(self):
        return self.hp
        ##complete this. return hp of the current object


def fusion(a, b):
    ##This function takes two Character objects as parameter
    ## Create a new object that has name equal to first-half of a's name + last-half of b's name
    ## Also new object's hp is the sum of a's hp + b's hp
    ##return the newly created object
    name1 =  a.getName()
    name2 = b.getName()
    n1_hp = a.getHp()
    n2_hp = b.getHp()
    n1_len = int(len(name1) / 2)
    n2_len = int(len(name2) / 2)
    n1_slice = name1[0:n1_len]
    n2_slice = name2[n2_len:]
    
    resString =  n1_slice + n2_slice
    resHp = int(n1_hp) + int(n2_hp)
    obj = Character(resString,resHp)
    return obj
def show(a): ##Already completed
    print(a.getName(), a.getHp()) ##printing the newobject's name and hp


#{ 
#Driver Code Starts.



def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        ##input object1
        Name1 = input()
        hp1 = int(input())
        boost1 = int(input())
        ##input object2
        Name2 = input()
        hp2 = int(input())
        boost2 = int(input())
        ##creating objects 1 and 2
        chara1 = Character(Name1, hp1)
        chara1.boost(boost1)
        
        chara2 = Character(Name2, hp2)
        chara2.boost(boost2)
        ##fuse and show the result
        show(fusion(chara1, chara2))
        testcases -= 1
        


if __name__=='__main__':
    main()
#} Driver Code Ends