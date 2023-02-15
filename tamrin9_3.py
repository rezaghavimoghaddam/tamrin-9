class Date():
    def __init__(self, y, m, d):
        self.y = y
        self.m = m
        self.d = d

    def show(self):
        print(self.y,"/",self.m,"/",self.d)

    def sum(self, d2):
        result = Date(None,None,None)
        result.y = self.y + d2.y
        result.m = self.m + d2.m
        result.d = self.d + d2.d
        if result.m > 12 :
            result.m -= 12
            result.y += 1
        if result.d > 30:
            result.d -= 30
            result.m += 1
        return result

    def sub(self, d2):
        result = Date(None,None,None)
        result.y = self.y - d2.y
        result.m = self.m - d2.m
        result.d = self.d - d2.d
        if result.m < 0 :
            result.m += 12
            result.y -= 1
        if result.d < 0:
            result.d += 30
            result.m -= 1
        if result.y < 0:
            result.y = -(result.y)
        return result

    def getmonthname(self):
        if self.m == 1:
            self.m = "farvardin"
        elif self.m == 2:
            self.m ="ordibehesht"
        elif self.m == 3:
            self.m ="khordad"
        elif self.m == 4:
            self.m ="tir"
        elif self.m == 5:
            self.m ="mordad"
        elif self.m == 6:
            self.m ="shahrivar"
        elif self.m == 7:
            self.m ="mehr"
        elif self.m == 8:
            self.m ="aban"
        elif self.m == 9:
            self.m ="azar"
        elif self.m == 10:
            self.m ="dey"
        elif self.m == 11:
            self.m ="bahman"
        elif self.m == 12:
            self.m ="esfand"
        print(self.y,self.m,self.d)

    def is_valid_date(self):

        if not 30 >= self.d >= 1  or not 12 >= self.m >= 1 or not 9999 >= self.y >= 1:
            print(False)
        else:
            print("Valid")
date1 = Date(2000, 5, 25)
date2 = Date(2023, 8, 12)
date3 = Date(2023, 2, 12)
date4 = Date(1995, 10, 14)
date5 = Date(1, 1, 0)
result_sum = date1.sum(date2)
print("Date sum: ")
result_sum.show()
result_sub = date3.sub(date4)
print("Date sub: ")
result_sub.show()
print("esme mah: ")
result_sum.getmonthname()
print("is valid date? ")
date5.is_valid_date()