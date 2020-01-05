# lets create a class Car and it has inner class Engine


class Car:

    def __init__(self,name,year):

        self.name = name
        self.year = year

    class Engine:

        def __init__(self , quique_number):
            self.quique_number = quique_number

        def display(self):
            return self.quique_number


c1 = Car("bmw" , 2019)  # making an object of class car

print(c1.name)
print(c1.year)

c2 = c1.Engine(231232312)  # making object for class engine , use object.inner_class , we make instance of inner class by using object of outer class and than inner class name
print(c2.display())  # invoking the method display



