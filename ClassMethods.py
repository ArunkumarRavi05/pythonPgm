class student:
    name = 'Tutor joes'
    age = 25
    def printall():
        print("Name :",student.name)
        print("Age  :",student.age)

student.printall()
print(student.__dict__)
print(getattr(student,'printall'))
getattr(student,'printall')()
student.__dict__['printall']()