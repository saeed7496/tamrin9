
class kasr:
    def __init__(self,a, b):
        self.s= a
        self.m= b

    def show(self):
        print(self.s,'/',self.m)

    def add(self,b):
        result=kasr(None,None)
        result.s=self.s*b.m + self.m*b.s
        result.m=self.m * b.m
        return result

    def mul(self,b):
        result=kasr(None,None)
        result.s=self.s*b.s
        result.m=self.m*b.m
        return result

    def sub(self,b):
        result=kasr(None,None)
        result.s=self.s*b.m - self.m*b.s
        result.m=self.m * b.m
        return result

    def div(self,b):
        result=kasr(None,None)
        result.s=self.s*b.m
        result.m=self.m*b.s
        return result


miz=kasr(4, 7)
sandali=kasr(5, 9)
c=sandali.div(miz)
c.show()











