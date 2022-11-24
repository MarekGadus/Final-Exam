import random
class Animal:
    def __init__(self,name,age=1,gender="Unknown",fedtimes=0):
        self.name=name
        self.age=age
        self.gender=gender
        self.fedtimes=fedtimes
        self.elephantchecks=0
    
    def eat(self):
        self.fedtimes+=1
        
    def isHungry(self):
        if self.name=="Lion":
            return True
        
        elif self.name=="Monkey":
            return random.choice([True, False])
        
        elif self.name=="Elephant":
            if self.elephantchecks%2==0:
                self.elephantchecks+=1
                return False
            else:
                self.elephantchecks+=1
                return True
            
            
            
    def toString(self):
        return (f'{self.name} is a {self.age} years old {self.gender} gender animal and was fed {self.fedtimes} times.')
    
    
class Worker(Animal):
    def __init__(self,name,animalsToLookAfter=[]):
        self.name=name
        self.animalsToLookAfter=animalsToLookAfter
        
    def doDailyRoutine(self):
        for animal in self.animalsToLookAfter:
            result=animal.isHungry()
            if result==True:
                animal.eat()
            else:
                pass
    def addAnimal(self,nameofanimal):
        self.animalsToLookAfter.append(nameofanimal)
            
Lion1=Animal("Lion")
Monkey1=Animal("Monkey")
Elephant1=Animal("Elephant")

Monkey2=Animal("Monkey")

worker1=Worker("Joe",[Lion1,Monkey1,Elephant1])
print(Elephant1.isHungry())

print(Elephant1.isHungry())
print(Elephant1.toString())



