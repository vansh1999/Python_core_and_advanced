# Polymorphism

# poly - multi
# morphism - behaviour

# we can have differnt behaviour(of method) based on differnt data(Objects)

# Differnt ways to impliment polymorphism
# 1. Duck typing , decendency injection
# 2. method overloading  -- > runtime polymorphism



# duck typing example 

'''
class Duck:
    def talk(self):
        print("quack quack")

class Human:
    def talk(self):
        print("hello")       

# duck typing,same function , will give different result with differnt object

def calltalk(obj):
    obj.talk()


d = Duck()
h = Human()


calltalk(d)   #same method but different ocjects
calltalk(h)
'''


# 1. dependency injection
# injection an object into another object

'''
                           |------  airbus
flight <-------- engine ---
                           |------  boing

'''
'''
class Flight:

    def __init__(self , engine):
        self.engine = engine

    def startengine(self):
        self.engine.Start() 

class Airbus():
    def Start(self):
        print("start the airbus engine")

class Boing():
    def Start(self):
        print("start the boing engine")


a1 = Airbus()
f1 = Flight(a1)
f1.startengine()


b1 = Boing()
f2 = Flight(b1)
f2.startengine()
'''


# 2. Method overriding   --- in inheritance we saw -- runtime polymorphism -- A subclass may change the functionality of a Python method in the superclass. It does so by redefining it. This is termed python method overriding.

# so what is overloading in python

# Method overloading --

'''
>>> def add(a,b):
      return a+b
>>> def add(a,b,c):
      return a+b+c
>>> add(2,3)

What looks like overloading methods, it is actually that Python keeps only the latest definition 
of a method you declare to it. This code doesn’t make a call to the version of add() that takes 
in two arguments to add. So we find it safe to say Python doesn’t support method overloading.

'''

'''
Check this out:

def add(a,b):
    return a+b

def add(a,b,c=0):    # using default
    return a+b+c
    
print(add(2,1))

### To that, we’ll say this isn’t method overloading, this is simply used of default arguments.

'''
# check this out too
'''
def add(instanceOf,*args):
      if instanceOf=='int':
              result=0
      if instanceOf=='str':
              result=''
      for i in args:
              result+=i
      return result

print(add('int',3,4,5))  
print(add('str','I ','speak ','Python'))


output - 12
output - I speak Python

'''