#Handling Multiple Exception in Python
try:
    a = 10/20
    print(a)
    b = [1,2,3,4]
    print(b[1])
    c=open("ramu.txt")
except ZeroDivisionError as e:
    print("Denominator cant be zero")
except IndexError as e:
    print("Invalid index")
except FileNotFoundError as e:
    print("File not found")