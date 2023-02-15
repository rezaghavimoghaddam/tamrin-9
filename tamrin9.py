class Kasr:
    def __init__(self, s, m):
        self.soorat = s
        self.makhraj = m

    def show(self):
        print(self.soorat, "/" ,self.makhraj)

    def mul(self, f):
        result = Kasr(None , None)
        result.soorat = self.soorat * f.soorat
        result.makhraj = self.makhraj * f.makhraj
        return result

    def sum(self, f):
        result = Kasr(None , None)
        result.soorat = (self.soorat * f.makhraj)+(self.makhraj * f.soorat)
        result.makhraj = self.makhraj * f.makhraj
        return result

    def sub(self, f):
        result = Kasr(None, None)
        result.soorat = (self.soorat * f.makhraj)-(self.makhraj * f.soorat)
        result.makhraj = self.makhraj * f.makhraj
        return result

    def div(self, f):
        result = Kasr(None ,None)
        result.soorat = self.soorat * f.makhraj
        result.makhraj = self.makhraj * f.soorat
        return result

f1 = Kasr(3 , 5)
f2 = Kasr(2 , 3)

result_mul = f1.mul(f2)
result_sum = f1.sum(f2)
result_sub = f1.sub(f2)
result_div = f1.div(f2)

result_mul.show()
result_sum.show()
result_sub.show()
result_div.show()