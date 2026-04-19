class Person:
    def __init__(self):
        self.name = ""
        self.age = 0

    def setInfo(self , nm, a):
        self.name = nm
        self.age = a

    def getInfo(self):
        print("Name  :", self.name)
        print("Age   :", self.age)


p1 = Person()
p2 = Person()
p3 = Person()

p1.setInfo("Akshay", 26)
p2.setInfo("Saurabh", 20)
p3.setInfo("Shrijeet", 25)

p1.getInfo()
p2.getInfo()
p3.getInfo()