"""
Print the space-separated name and email address pairs containing valid email addresses only. Each pair must be printed on a new line in the following format:

name <user@email.com>
You must print each valid email address in the same order as it was received as input.

Sample Input

2  
DEXTER <dexter@hotmail.com>
VIRUS <virus!@variable.:p>
Sample Output

DEXTER <dexter@hotmail.com>
Explanation

dexter@hotmail.com is a valid email address, so we print the name and email address pair received as input on a new line.
virus!@variable.:p is not a valid email address because the username contains an exclamation point (!) and the extension contains a colon (:). As this email is not valid, we print nothing.
"""
import re
#^[a-zA-Z]*[0-9_\-.]*@[A-Za-z]*.[A-Za-z]{1,3}$
if __name__ == '__main__':
    n = int(input())
    
    for _ in range(n):
        name, mail = (map(str , input().split()))
        lenMail = int(len(mail)) - 1
        s = mail[1:lenMail]
        m = re.search(r'^[a-zA-Z][a-z0-9_\-.]*@[A-Za-z]*(\.)[A-Za-z]{1,3}$$',s)
        if(bool(m)):
            print(name,mail)
