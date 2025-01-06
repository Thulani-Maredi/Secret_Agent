# Program to convert the given date into the correct format
# Thulani Maredi
# mrdthu003
# 21 March 2024

date = input("Enter the date and time (yyyy-mm-dd hh:mm):\n")


months = ['January','February','March','April','May','June','July','August','September','October','November','December']
day_suffix = ['st','nd','rd','th']
time_suffix = ['am','pm']

dates = date.split(" ") # split the dates and time into a list
info = dates[0].split("-") # split the dates into months, days and years
value1 =  int(info[1]) # choose the months in the list of dates
month = months[value1-1] 
value2 = int(info[2]) # choose the days in the list of dates 
stringday = str(value2) # make the days into strings
if stringday==1 or stringday[1]==1: # if statements to provide suffix to the days 
    stringday += "st"
elif stringday==2 or stringday[1]==2:
    stringday += "nd"
elif stringday==3 or stringday[1]==3:
    stringday += "rd"
else: 
    stringday += "th"
    
time = dates[1].split(":") # go into the dates list and choose the time then seprate it into hours and minutes
hour = int(time[0]) 
minutes = time[1]
if hour > 12 : # if statements to provide the correct suffix to the time part of the stamenent 
    hour = hour -12
    hour = str(hour)+":"+minutes+" pm "
elif hour == 00 :
    hour = "12:"+minutes+" am "
elif hour == 12:
    hour = "12:"+minutes+" pm "
else:
    hour = str(hour)+":"+minutes+" am "
    
year = info[0] # go into the list of separated dates and collect only the year
year = " '"+year[2:] # collect only the last two digits of the year 

print(hour+"on the "+stringday+" of "+month+year) 