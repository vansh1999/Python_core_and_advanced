# 1. Encapsulation - In encapsulation code and date are wrapped together within a single unit
#                    from being modifield by accient.
#                    we restrict access to methods and variables. this prevent data
#                    from direct modification.

# think of it as capsule

# capsule - class
# propertis/variables
# functionalities/method


# encapsulation - binding all data in an class(capsule) and protecting it from outside access


# 1. private fields

# we make them private by using '__' , two underscore in front of variable to make it private



# class Student:

#     def __init__(self,name,iid):

#         self.__name = name   # made name private by using __
#         self.__iid = iid     # made iid private by using __

#     def display_name(self):
#         return self.__name  # to get the private name field

#     def display_iid(self):
#         return self.__iid   # to get the private iid field

# # s = Student("vansh" , 121)
# # print(s.name)
# # print(s.iid)  gives error , AttributeError: 'Student' object has no attribute 'name'

# s = Student("vansh" , 34)
# print(s.display_name())
# print(s.display_iid())




# name mangling - synatx to access the private fields
# even it is private field we can still access the files using synatx called name mangling
# _className___fieldName

# class Student:

#     def __init__(self,name,iid):

#         self.__name = name   # made name private by using __
#         self.__iid = iid     # made iid private by using __


# s = Student("vansh" , 121)
# print(s._Student__name) # able to access the priavte field, name mangling
# print(s._Student__iid)  #


# Python supports most of the terms associated with "objected-oriented" programming language except strong encapsulation.


# how to empliment encapsulation in python, use getter and setters method to access and change, and make them private


class Car:

    def __init__(self,name , iid):

        self.__name = name   # made name and iid private by using __
        self.__iid = iid


    def set_iid(self , value):  # setter method to set iid
        self.__iid = value

    def get_iid(self):   # getter method to dispay iid method
        return self.__iid


c = Car("ford" , 3424)   

c.set_iid(1000)    # set method
c.__iid = 2000     # tried to change the value, can't change due to encapsulation

print(c.get_iid())


