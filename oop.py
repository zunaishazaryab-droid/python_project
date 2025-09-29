class Car:
    name="BMW"
    color="Black"
    wheels=4
    def forward(self):
        print("car is about to be forwarded")
obj=Car()
obj.forward()
print(obj.name)
print(obj.color)
print(obj.wheels)



class Computer:
    def __init__(self,company,model,color):
        self.company=company
        self.model=model
        self.color=color
    def quailty(self):
        print("this is best quailty of computer")
obj=Computer("hp","i2","black")
obj.quailty()
print(obj.company)
print(obj.model)
print(obj.color)





class Car:
    def __init__(self,model,company):
        self.model=model
        self.company=company
    def forward(self):
        print("car is about to be forwarded")
    @staticmethod
    def booster_mode():
        print("you erobled the booster mode")
obj=Car("12ADBG","BMW")
obj.forward()
print(obj.company)
print(obj.model)
Car.booster_mode()




class Computer:
    def __init__(self,company,model,color):
        self.company=company
        self.model=model
        self.color=color
        self.__hardware_type="Type A"
    def hardware_type(self):
        print("this is hardware type")
obj=Computer("hp","i2","black")
print(obj.company)
print(obj.model)
print(obj.color)



class Car:
    def __init__(self,door,seats,color):
        self.door=door
        self.seats=seats
        self.color=color
    def forward(self):
        print("car is about to be forwarded")
class BMW(Car):
    def __init__(self,model,doors,seats,color):
        super().__init__(doors,seats,color)
        self.model=model
    def price(self):
        print("this is price")
obj=BMW("12asb",4,6,"red")
obj.forward()
obj.price()
print(obj.model)
print(obj.color)
print(obj.seats)
print(obj.door)















