'''
class student:
    name = 'Tutor Joes'
    age = 25
    def printall(self):
        print(student.name," age is ",student.age)
o = student()
o.printall()
student.printall(o)
'''

#Adding new attribute
class student:
    name = 'Tutor Joes'
    age = 25
    def printall(self,gender):
        print("Name    :",student.name)
        print("Age     :", student.age)
        print("Gender  :", gender)
o = student()
o.printall('Male')
#student.printall(o.'Male')