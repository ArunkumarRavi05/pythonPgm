# Fine for library book delay

days = int(input("Enter delayed days :"))
if(days == 0):
    print("Good no fine.")
elif(days>=1 and days<=5):
    print("Fine amount : Rs.",0.5*days)
elif(days>5 and days<=10):
    print("Fine amount : Rs.",1*days)
elif(days>10 and days<=30):
    print("Fine amount : Rs.",5*days)
else:
    print("Menbership cancelled.")
