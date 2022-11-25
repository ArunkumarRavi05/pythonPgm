#Else part execute only when loop executed fully

for i in range(10):
    print(i)
    i+=1
else:
    print("For loop completed")



for i in range(10):
    if i==6:
        break
    print(i)
    i+=1
else:
    print("For loop completed")
