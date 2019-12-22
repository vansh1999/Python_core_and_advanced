# def main():
#     print("hello world")

# print("guru99")  

# main()


'''
function "if__name__== "__main__".

When Python interpreter reads a source file, it will execute all the code found in it.
When Python runs the "source file" as the main program, it sets the special variable (__name__) to have a value ("__main__").
When you execute the main function, it will then read the "if" statement and checks whether __name__ does equal to __main__.
In Python "if__name__== "__main__" allows you to run the Python files either as reusable modules or standalone programs.

'''

# def main():
#     print("hello this is main function")


# if __name__ == "__main__":
#     main()


# print("oh guru")

# SO MAIN IS THE FIRST TO EXECUTE IN FILE/MODULES SAME LIKE C/C++/JAVA


# import Calc  < ---------out -- calc says Calc

# print("demo says " , __name__)  ---- demo says demo


def first():
    print("hello")
    print("user")


if __name__ == "__main__":
    first()


print("login section")