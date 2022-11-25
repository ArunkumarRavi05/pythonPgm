class father:
    def fishing(self):
        print("learn fishing")
class mother:
    def cooking(self):
        print("learn cooking")
class son(father,mother):
    def coding(self):
        print("learn coding")

o = son()
o.fishing()
o.cooking()
o.coding()