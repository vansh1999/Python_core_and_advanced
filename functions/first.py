# 1 -- > defination of function

def func(a,b):
    return (a+b)/2


# 2 -- > invocation of function

print(func(10,10))


# returning multiple values

def opera(a,b):

    fir = a+b
    sec = a-b
    thi = a * b

    return fir,sec,thi # <-- retured and stored as tuple

print(opera(2,5))    

result = opera(2,5)

for i in result:
    print("answer" , i)




# display1()   

# # assign function to variable

# zi = display1 #---- no () in display()
# # print("this is ziii ", zi())   # <---() in zi

# # print("this is ziii {}".format( zi()))

# zi()



# function inside the another function

def dis(name):
    def message():
        return "hello"
    result = message() +" " + name
    return result

print(dis("vansh"))    



# returing functions


def dis():
    def message():
        return "hello"

    return message 

fun = dis()
print(fun())       
    

# keyword argument

def func(a , b):

    print(a)
    print(b)

func( b = 100 , a = 1)   



# default arguments

# def summing(a , b):
#     return a + b


# print(summing())  <---- error TypeError: summing() missing 2 required positional arguments: 'a' and 'b'


def summing(a = 10 , b = 20) :
    return a + b


print(summing())

# now it will return 30 as argumenst are passed in function defination not in invocation

# PARAMETER(INVOCATION) > PARAMETER(DEFINATION)


def adding(a = 1 ,b = 2):
    return a + b

print(adding())
print(adding(10,20)) 


# PARAMETER(INVOCATION) > PARAMETER(DEFINATION)