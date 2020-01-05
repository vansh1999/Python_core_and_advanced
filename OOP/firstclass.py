
class Person:   # class name

    def __init__(self):    # initilize/constructor, self - > points to the current object that is being created , p1.name , p1.age etc.
        self.name = "vansh"
        self.age = 20
        self.rich = "yes"


p1 = Person()   # class name
 
print(p1.name)  # access method properties
print(p1.age)
print(p1.rich)


# now use parametrised constructors


class Products:

    def __init__(self , na , ra):  # parametrised constructors
        self.name = na
        self.ratings = ra


p1 = Products("abc" , 3.5)
p2 = Products("xyz" , 4.8)

print(p1.name)
print(p1.ratings)

print(p2.name)
print(p2.ratings)





