class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den =  bottom

    def show(self):
        print(self.num, " / ", self.den)

    def __str__(self):
         return str(self.num) + "/" + str(self.den)

    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newdem = self.den * otherfraction.den
        common = self.gcd(newnum, newdem)
        return (Fraction(newnum // common, newdem // common))

    def __eq__(self, other):
        fnum = self.num*other.den
        sdem = self.den*other.num

        return fnum == sdem

    def gcd(self,m, n):
        while m%n != 0:
            oldm = m
            oldn = n

            m = oldn
            n = oldm%oldn
        return n

myfac = Fraction(1, 4)
myfac2 = Fraction(1, 2)
print(myfac + myfac2)
myfac.show()
print(myfac)
print(myfac == myfac2)