class student:
    def __init__(self,total):
        self._total = total

    def average(self):
        return self._total/5.0


    def getters(self):
        return self._total


    def setters(self,t):
        if t<0 or t>500:
            print("Invalid total and cant change")
        else:
            self._total=t

total = property(getters,setters)

o = student(450)
print("Total :",o.total)
print("Average :",o.average())
o.total = 350
print("Total :",o.total)
print("Average :",o.average())
