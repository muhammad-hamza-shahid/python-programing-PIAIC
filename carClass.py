class Car():
    def __init__ (self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def description(self):
        print(f"The make of this car is {self.make}")
        print(f"The model of this car is {self.model}")
        print(f"The year of this car is {self.year}")
    def move(self):
        print(f"{self.make} is moving forward with speed")
    def carBreak(self):
        print(f"{self.model} hav very good breaking system")

    def completeInfo(self):
        owner = Owner("hamza","23")
        return owner.name,self.make,self.model

class Owner():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def getName(self):
        return self.name
    def getAge(self):
        return self.age


car1=Car("Honda","City","2020")
print(car1.description())
print(car1.model)

tt = car1.completeInfo()
print(f"{tt[0]} is the owner of {tt[1]} and the model of his car is {tt[2]}")
print(car1.completeInfo())


