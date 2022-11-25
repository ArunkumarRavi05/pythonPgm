m1 = int(input("Enter mark1 :"))
m2 = int(input("Enter mark2 :"))
m3 = int(input("Enter mark3 :"))
total = m1+m2+m3
print("Total :",total)
avg = total/3.0
print("Average :",avg)
if m1>=35 and m2>=35 and m3>=35 :
    print("Result : PASS")
    if avg>=90 and  avg<=100 :
        print("Grade : A")
    elif avg>=80 and  avg<=89 :
        print("Grade : B")
    elif avg>=70 and  avg<=79 :
        print("Grade : C")
    else:
        print("Grade : D")
else:
    print("Result : FAIL")
    print("Grade : No Grade" )