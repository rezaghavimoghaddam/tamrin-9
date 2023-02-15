class Time():
    def __init__(self,h, m, s):
        self.h = h
        self.m = m
        self.s = s

    def show(self):
        print(self.h,":",self.m,":",self.s)

    def sum(self, t):
        result = Time(None ,None ,None)
        result.h = self.h + t.h
        result.m = self.m + t.m
        result.s = self.s + t.s
        if result.m >= 60:
            result.m -= 60
            result.h += 1
        if result.s >= 60:
            result.s -= 60
            result.m += 1
        if result.h >= 24:
            result.h -= 24
        return result

    def sub(self, t):
        result = Time(None, None, None)
        result.h = self.h - t.h
        result.m = self.m - t.m
        result.s = self.s - t.s
        if result.m <= 60:
            result.m += 60
            result.h -= 1
        if result.s <= 60:
            result.s += 60
            result.m -= 1
        if result.h >= 24:
            result.h += 24
        if result.h < 0:
            result.h += 24
        return result
    def tabdil_s_to_d(self):
        while True:
            if self.s >= 60:
                self.s -= 60
                self.m += 1
            if self.m >= 60:
                self.m -= 60
                self.h += 1
            if self.s < 59 and self.m < 59:
                break
        print(self.h,":",self.m,":",self.s)

    def tabdil_d_to_s(self):
        while True:
            if self.h > 0:
                self.h -= 1
                self.m += 60
            if self.m > 0 :
                self.m -= 1
                self.s += 60
            if self.h == 0 and self.m == 0:
                break
        print(self.h,":",self.m,":",self.s)

time1 = Time(10 ,25 ,33)
time2 = Time(15 ,40 ,45)
time3 = Time(0,0,13748)
sum_result = time1.sum(time2)
print("sum:")
sum_result.show()
sub_result = time1.sub(time2)
print("sub")
sub_result.show()
print("tabdil sanie be tarikh:")
time3.tabdil_s_to_d()
print("tabdil tarikh be sanie:")
time1.tabdil_d_to_s()