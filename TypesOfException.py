print(dir(locals()['__builtins__']))
print(len(dir(locals()['__builtins__'])))

# 1.NameError Exception
try:
    print(a)
except NameError as e:
    print("A is not defined")


# 2.ZeroDivisionError Exception
try:
    a=10/0
except ZeroDivisionError as e:
    print("Denominator cant be Zero")

# 3.ValueError Exception
try:
    a=int("joes")
except ValueError as e:
    print("Please enter number only")

# 4.IndexError Exception
try:
    a = [1,2,3,4]
    print(a[10])
except IndexError as e:
    print("Invalid index")

# 5.FileNotFound Exception
try:
    f=open("test.txt")
except FileNotFoundError as e:
    print("File not found")
else:
    print(f.read())
