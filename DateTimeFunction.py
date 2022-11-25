import datetime as dt
current_date = dt.date.today()
print("current Date :",current_date)

#To create new Date
new = dt.date(2021,10,25)
print(new)
print("Year  :",new.year)
print("Month :",new.month)
print("Day   :",new.day)

##                              TIME
a = dt.time(10,45,5,5050)
print(a)
print("Hour        :",a.hour)
print("Minute      :",a.minute)
print("Second      :",a.second)
print("Microsecond :",a.microsecond)


#For current time
current_time = dt.datetime.now()
print("Current time :",current_time)


#To create new time
new = dt.datetime(2021,5,31,12,2,10)
print(new)
print("Date :",new.date())
print("Time :",new.time())

#To find Difference between 2 dates
current = dt.datetime.now()
new_year =dt.datetime(2023,1,1)
difference = new_year-current
print(difference)

#Formatting Date and Time
s=current.strftime("%A %B %d %Y")
print(s)

