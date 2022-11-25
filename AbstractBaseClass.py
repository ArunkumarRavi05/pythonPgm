from abc import ABC,abstractmethod
class Bank(ABC):
    @abstractmethod
    def loan(self):
        pass

    @abstractmethod
    def credit(self):
        pass

    @abstractmethod
    def debit(self):
        pass

class HDFC(Bank):
    def loan(self):
        print("HDFC provide loan @ 7.5%")
    def credit(self):
        print("HDFC provide credit")
    def debit(self):
        print("HDFC provide debit")
    def card(self):
        print("HDFC provide credit card")

o = HDFC()
o.loan()
o.credit()
o.debit()
o.card()