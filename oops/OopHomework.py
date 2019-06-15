import math
class Line:

    def __init__(self,coord1, coord2):
        self.coord1 = coord1
        self.coord2 = coord2

    def distance(self):
        return (math.sqrt((self.coord2[1]-self.coord1[1])**2 + (self.coord2[0]-self.coord1[0])**2))

    def slope(self):
        return ((self.coord2[1]-self.coord1[1])/(self.coord2[0]-self.coord1[0]))


class Bank:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account owner: {self.owner} \nAccount Balance: {self.balance}"

    def withraw(self,amt):
        if (self.balance - amt) < 0:
            print(f"{self.owner} has only {self.balance} in balance. So cananot withraw {amt} amount.")
        else:
            self.balance = self.balance - amt
            print(f"{self.owner} is withdraw {amt}. Available balance is {self.balance}")

    def deposit(self,deposit):
        self.balance = self.balance + deposit
        print(f"Available balance is {self.balance}")


acct1 = Bank('Jose',100)
print(acct1)
acct1.owner
acct1.balance
acct1.deposit(50)
acct1.withraw(75)
acct1.withraw(80)






coordinate1 = (3,2)
coordinate2 = (8,10)
myline = Line(coordinate1, coordinate2)
print(myline.distance())
print(myline.slope())
