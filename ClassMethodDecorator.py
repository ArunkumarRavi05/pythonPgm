class student:
    count = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        student.count +=1

    def printDetails(self):
        print("Name : ",self.name, " Age :",self.age)

    @classmethod
    def total(cls):
        return cls.count

o = student("Joes",25)
o.printDetails()
print("Total Admission :",o.total())
a = student("Raja",35)
o.printDetails()
print("Total Admission :",o.total())
print("Total Admission :",student.total())