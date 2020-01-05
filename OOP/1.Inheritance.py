# Interitance

'''
    existing object
        ^
        |
        |    (new object inheriting properties of existing object)
        |
        |
    new object   

'''
# 1. how to inherit field from existing class
# 
''' 
class Bmw:

    def __init__(self, name, year):
        self.name = name
        self.year = year

class threeSer(Bmw):
    def __init__(self, automatic , name , year):
        Bmw.__init__(self,name,year)  
        self.automatic = automatic  

class fiveSer(Bmw):
    def __init__(self , boost , name , year):
        Bmw.__init__(self,name , year)
        self.boost = boost

t1 = threeSer("yes" , "bmw" , 2019)
print(t1.automatic)  

t2 = fiveSer(300 , "bmw" , 2019)
print(t2.boost)
'''

# 2. how to inherit methods from a parent class

'''
class Bmw:
    
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def Starting(self):
        return "starting the car"   
    def Stopping(self):
        return "stopping the car"        

class threeSer(Bmw):
    def __init__(self, automatic , name , year):
        Bmw.__init__(self,name,year)  
        self.automatic = automatic  


c1 = threeSer("ys" , "bmw" , 2019)
print(c1.name)

# using parent class method in child class
print(c1.Starting())
print(c1.Stopping())
'''


# What is OverRiding

# sometimes child class want to use same methods of parent class but with differnt functionality

#

'''
class Bmw:
    
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def Starting(self):
        return "starting the car"   
    def Stopping(self):
        return "stopping the car"        

class threeSer(Bmw):
    def __init__(self, automatic , name , year):
        Bmw.__init__(self,name,year)  
        self.automatic = automatic  

    def Starting(self):      # method overriding 
        return "starting three series bmw car"


c1 = threeSer("yes" , "bmw" , 2019)
print(c1.Starting())   # we get overriden result, 
print(c1.Stopping())  # simple parent method
 
'''

# method overriding - using same method as of parent class and impliminting own functionalities




# 4. use of Super()

# make Parent class as super and 
# 1. instead of Bmw.__init__(self,name,year) ---> use super().__init(name,year)
# 2. can implement functionalities of parent class

'''
class Bmw:
    
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def Starting(self):
        return "starting the car"   
    def Stopping(self):
        return "stopping the car"        

class threeSer(Bmw):
    def __init__(self, automatic , name , year):
        super().__init__(name,year)      # instead of bmw() use Super and remove self
        self.automatic = automatic  

    def Starting(self): 
        print(super().Starting())            # 2. implementing functionalities of parent class
        print("starting three series bmw car")


c1 = threeSer("yes" , "bmw" , 2019)


c1.Starting()
'''