class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def printDetails(self):
        print("Name :",self.name," Age :",self.age)

    @staticmethod
    def welcome():
        print("Welcome to out institution")

s1 = student('Tutor',25)
s1.printDetails()
s1.welcome()

s2 = student('Raja',45)
s2.printDetails()
s2.welcome()