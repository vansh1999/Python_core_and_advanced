
glo  = 100

def func():
    y = 10
    return y , glo
    


print(glo)

print(func())

# print(y) < -- error


#  global and local presidence

x = 123

def display():
    x=6000
    print(x)

print(x)   # < --- returns global
display()    # < -- return function variable

# so how to display global in function variable

def display1():
    print(globals()['x'])  # use globals()['var-name']

display1()   

# assign function to variable

zi = display1 #---- no () in display()
# print("this is ziii ", zi())   # <---() in zi

# print("this is ziii {}".format( zi()))

zi()


