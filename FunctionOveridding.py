class Employee:
    def workingHrs(self):
        self.Hrs = 50

    def printHrs(self):
        print("Employee working Hours :",self.Hrs)

class Trainee(Employee):
    def workingHrs(self):
        self.Hrs = 60

    def resetHrs(self):
        super().workingHrs()

employee =Employee()
employee.workingHrs()
employee.printHrs()

trainee = Trainee()
trainee.workingHrs()
trainee.printHrs()
trainee.resetHrs()
trainee.printHrs()