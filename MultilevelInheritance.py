class grandfather:
    def house(self):
        print("has own house")
class father(grandfather):
    def car(self):
        print("has own car")
class son(father):
    def book(self):
        print("has own book")

o = son()
o.house()
o.car()
o.book()