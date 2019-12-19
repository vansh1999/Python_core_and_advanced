# no need to declare the numberic type
a = 15
print(a)

print(type(a))
# o/p - <class 'int'> , shows everything is stored as the class in python

b = 15.0

print(b)
print(type(b))
# float

c = True

print(type(c))
# bool

# type conversion -->


d = float(a)

print(d)
print(type(d))


h = float("33")
print(h)
# 33.0

# h = float("vansh")
# print(h)
# ValueError

bina = bin(4)
print(bina)