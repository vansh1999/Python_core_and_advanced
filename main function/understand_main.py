# Defining Main Functions in Python


# Many programming languages have a special function that is automatically executed when an
# operating system starts to run a program. This function is usually called main() and must 
# have a specific return type and arguments according to the language standard. On the other hand, 
# the Python interpreter executes scripts starting at the top of the file, and there is no specific
#  function that Python automatically executes.

# Nevertheless, having a defined starting point for the execution of a program is useful
#  for understanding how a program works. Python programmers have come up with several conventions 
#  to define this starting point.

# A Basic Python main()

# def firstmethod():
#     print("Hello World!")

# if __name__ == "__main__":
#     firstmethod()





'''
# a = 10
# if __name__ == "__main__":
#     print("main")

# mainin() 

# if __name__ == "__main__":
#             got = "Game of Thrones is a legendary shown"
#             print(got)

'''
# In the above example, the conditional if statement is going to compare the values of the 
# variable __name__ with the string “__main__“. If, and only if it evaluates to True, 
# the next set of logical statements are executed. Since we are directly running the program, 
# we know that the conditional statement is going to be True. Therefore, the statements are 
# executed, and we get the desired output. In this way, we can use the __name__ variable to control 
# the execution of your code. You may refer to the output displayed below:


'''

# 

# def adding_fun(a,b):
#     return a + b

# def sub_fun(a,b):
#     return a - b


# if __name__ == "__main__":
#         a , b = map(int , input("add two nums: ").split())
#         print(adding_fun(a,b))
        
#         a , b = map(int , input("sub two nums: ").split())
#         print(sub_fun(a ,b))
        
 '''       
        