'''

Decorators in Python

A decorator is a design pattern in Python that allows a user to add new functionality
to an existing object without modifying its structure. Decorators are usually called before
the definition of a function you want to decorate.

Functions in Python are first class citizens. This means that they support operations such as being passed as an argument, returned from a function, modified, and assigned to a variable. This is a fundamental concept to understand before we delve into creating Python decorators.

1. Assigning Functions to Variables
2. Defining Functions Inside other Functions
3. Passing Functions as Arguments to other Functions

def plus_one(number):
    return number + 1

def function_call(function):
    number_to_add = 5
    return function(number_to_add)

function_call(plus_one)
output - 6

4. Functions Returning other Functions
5. Nested Functions have access to the Enclosing Function's Variable Scope
Python allows a nested function to access the outer scope of the enclosing function. 
This is a critical concept in decorators -- this pattern is known as a Closure.

def print_message(message):
    "Enclosong Function"
    def message_sender():
        "Nested Function"
        print(message)

    message_sender()

print_message("Some random message")

output -- Some random message


'''

# Creating decorators
'''
def upper_decor(function):

    def wrapper():
        fun = function()
        make_uppercase = fun.upper()
        return make_uppercase

    return wrapper

# ----------------------
# def say_hi():
#     return "hello there!"


# decorate = upper_decor(say_hi)
# print(decorate())
# ----------------------------
# this can be -- 

@upper_decor
def say_hi():
    return "hello there!"

print(say_hi())    


'''


# def decorfun(fun):
#     def inner(n):
#         result = fun(n)
#         result += " how are yo ?"
#         return result
#     return inner    

# @decorfun
# def hello(name):
#     return " hello " + name

# print(hello("vansh "))    


