"""
https://docs.python.org/3/library/datetime.html

When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to view this new post on their news feed. Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.

Since sometimes posts are published and viewed in different time zones, this can be confusing. You are given two timestamps of one such post that a user can see on his newsfeed in the following format:

Day dd Mon yyyy hh:mm:ss +xxxx

Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.

Sample Input 0

2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000
Sample Output 0

25200
88200

                   

>>> datetime.date.today()
datetime.date(2022, 5, 24)
>>> d = datetime.date.today()
>>> d
datetime.date(2022, 5, 24)
>>> import datetime
>>> d = datetime.date.today()
>>> d
datetime.date(2022, 5, 24)
>>> m = datetime.date(1992, 5, 24)
>>> d-m
datetime.timedelta(days=10957)
>>> (d-m)/365
datetime.timedelta(days=30, seconds=1656, microseconds=986301)
>>> (d-m) // 365
datetime.timedelta(days=30, seconds=1656, microseconds=986301)
>>> 10957 // 365
30

today = datetime.date.today()
df = today.strftime('%Y-%b-%d')               
"""
from datetime import datetime as dt

#s = '10 May 2015'
# dd Mon yyyy 
fmt = '%d %b %Y'
for i in range(int(input())):
    print(int(abs((dt.strptime(input(), fmt) -
                   dt.strptime(input(), fmt)).total_seconds())))
