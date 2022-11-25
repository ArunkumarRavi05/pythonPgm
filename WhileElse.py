#Else part execute only when loop executed fully

i=1
while i<=10:
    print(i)
    i+=1
else:
    print("While loop completed")


i=1
while i<=10:
    if i==5:
        break
    print(i)
    i+=1
else:
    print("While loop completed")
