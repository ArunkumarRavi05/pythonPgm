class student:
    name = "Ram kumar"
    age = 25

#getattr method

print(getattr(student,'name'))
print(getattr(student,'age'))
print(getattr(student,'gender','No such attribute found'))

#Dot notation
print(student.name)
print(student.age)

# To Modify or Update

#setter method
setattr(student,'name','Tutor joes')
print(student.name)

setattr(student,'gender','Male')
print(student.gender)

#Dot notation to create new attribute
student.city ='salem'
print(student.city)
print(student.__dict__)

#Delete
delattr(student,'city')
print(student.__dict__)
delattr(student,'gender')
print(student.__dict__)
