# class Calculator:
#     a, b, c = 0, 0, 0
#     def setdata(self, a, b):
#         self.a = a
#         self.b = b

#     def add(self):
#         self.c = self.a + self.b

# calc = Calculator()
# calc.setdata(10, 20)
# calc.add()
# print(calc.c)
         

class Calculator:
    a, b, c = 0, 0, 0
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        self.c = self.a + self.b

calc = Calculator(30, 40)
calc.add()
print(calc.c)
