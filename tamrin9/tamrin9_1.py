
from unittest import result


class time:
    def __init__(self, hour, minute, second):
        self.h=hour
        if minute<=60 and second<=60:
            self.m=minute
            self.s=second
        else:
            print('time not availble')
    def show_time(self):
        print(self.h,':',self.m,':',self.s)

    def add(self, b):
        result=time(0, 0, 0)
        result.h=self.h+b.h
        result.m=self.m+b.m
        result.s=self.s+b.s
        if result.s>=60:
            result.s-=60
            result.m+=1
        if result.m>=60:
            result.m-=60
            result.h+=1
        return result

    def sub(self,b):
        result=time(0, 0, 0)
        result.h=self.h-b.h
        result.m=self.m-b.m
        result.s=self.s-b.s
        if result.s<=0:
            result.s+=60
            result.m-=1
        if result.m<=0:
            result.m+=60
            result.h-=1
        return result        

    def change2second(self):
        result=time(0, 0, 0)
        result.s=self.h*3600+self.m*60+self.s
        return result

    def change2time(self,b):
        result=time(0, 0, 0)
        result.h=b//3600
        result.m=(b%3600)//60
        result.s=(b%3600)%60
        return result

pen=time(8,25,13)
car=time(11, 39, 59)
c=pen.change2second()
c.show_time()
x=car.change2time(30313)
x.show_time()






