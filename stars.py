"""
Stark is a 10 year old kid and he loves stars. So, he decided every day he will capture a picture of a sky. After doing this for many days he found very interesting observations.

Every day the total number of stars in the sky is same as days completed for a calendar year. He noticed, on Saturday's and Sunday's that there are no stars in the sky. Stark's camera does not have wide angle capture feature so he could only capture maximum of 50 stars at a time. So, he assumed that there are only 50 stars in the sky that day. Also, the camera discharges every 4th day and he is not be able to click any picture that day. So let's say, if the first day of calendar (01/01/0001) starts on a Monday then on Thursday he can't click any pictures. Then resuming on Friday he can take pictures until Sunday, but can't take picture on Monday, followed by downtime on Friday, then Tuesday, then Saturday etc. When the camera discharges he considers 0 stars that day.

You are his programmer friend and want to help him. You need to write a code which will tell him on a particular date how many stars Stark's camera was able to click.

You can assume Stark has an ancient camera and your first input will be the day for date (01/01/0001) and then followed by any date on which Stark wants to find out the number of stars in the sky."""


import datetime
from datetime import date
day=input()
try:
	if day=="Saturday" or day=="Sunday":	
		date=list(map(int,input().split("/")))
		print ("0")
	elif day=="Monday" or day=="Tuesday" or day=="Wednesday" or day=="Thursday" or day=="Friday":
		date=list(map(int,input().split("/")))
		
		d1 = datetime.datetime(0o001,0o1,0o1)
		d2 = datetime.datetime(date[2],date[1],date[0])
		if ((((d2-d1).days)+1)%4)==0:
			print ("0")
		else:
			if date[1]>2:
				print ("50")
			elif date[1]==2 and date[0]>19:
				print ("50")
			elif date[1]==2 and date[0]<=19:
				print (31+date[0])
			elif date[1]==1:
				print (date[0])
	else:
		print ("Invalid Day")
except:
	print ("Invalid Date")
