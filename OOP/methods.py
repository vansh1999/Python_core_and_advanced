'''
instance method/plain vs @staticmethods vs @classmethod

1. Instance method
   ** can modify object instance state
   ** can modify class state 

2. Class Method
   * can't modify object instance state
   ** can modify class state

3. Static Method
   * can't modify object instance state
   * can't modify class state   

'''

'''
# 1. Instance Method


class Student:

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2   <--- m1,m2,m3 are instance variable
        self.m3 = m3  

    def avg(self):   # <-- this is an instance method, because it has 'self' , when we say self, it means it belongs to a particular object.so if you have to call an avg() you have to say s1.avg() or s2.avg(). we cannt simply say Student.avg()
        return (self.m1 + self.m2 + self.m3) / 3 

    def getm1(self):  # writing get is not nessary, just convention
        return self.m1   

    def setm1(self , m1):
        self.m1 = m1




s1 = Student(23,23,65)
s2 = Student(45,66,89)


print(s1.avg())
print(s2.avg())

# getter/accessor for s1,s2

print("m1 for s1 is" , s1.getm1())



# setter/mutators for s1,s2

'''

# In instance we have two different types -- getters and setters

# getters - methods used fetch the data  aka - accessor methods
# setters - methods that are used to change the data aka - mutator methods

# see how getters and setters are used

# class Student:
    
#     school = "SET"

    # def __init__(self,m1,m2,m3):

    #     self.m1 = m1
    #     self.m2 = m2
    #     self.m3 = m3


#     def set_marks1(self , m1):
#         self.m1 = m1
        

#     def get_marks1(self):
#         return self.m1


# s1 = Student()
# s1.set_marks1(60)

# print(s1.get_marks1())







# 2. class method

# class method uses class variable
# uses cls instead of self

'''
class Student:

    school = "SET"

    def __init__(self,m1,m2,m3):

        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):  #instance method
        return (self.m1 + self.m2 + self.m3) / 3 

    @classmethod
    def getschool(cls):
        return cls.school


s1 = Student(23,23,23)

print(s1.getschool())

# but all this is class method , instead of s1,s2.. it should work for Student as well, let's see

# print(Student.getschool()) , but get error ,TypeError: info() missing 1 required positional argument: 'cls'
    
# so have to use @classmethod before info

# now no problem
print(Student.getschool())
'''



#3. static methods


# when method has nothing to do with class variables or method variables , we may
# keep method as blank , no self or cls
'''
class Student:
    
    school = "SET"

    def __init__(self,m1,m2,m3):

        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):  #instance method
        return (self.m1 + self.m2 + self.m3) / 3 

    @classmethod
    def getschool(cls):
        return cls.school


    @staticmethod
    def sum_method():
        return 'sum of 2 and 2 is' ,  2+2


s1 = Student(23,23,22)

print(s1.sum_method())
'''