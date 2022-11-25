try:
    a=10/0
except Exception as e:
    print(e)

#try except else in python
try:
    a=10/8
except Exception as e:
    print(e)
else:
    print("A value :",a)

#try except else finally
try:
    a=10/2
except Exception as e:
    print(e)
else:
    print("A value :",a)
finally:
    print("Thank you")