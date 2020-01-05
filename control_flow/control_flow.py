#  if elif else statement

x = 15

if x < 0: print("negative")

elif x > 0: print("positive")

elif x == 0: print("zero")

else: print("enter valid number")



# while

"""
while expression:
    statement(s)

"""


count = 0
while x > 0:
    x = x//2
    count += 1
print(count)


# do-while 

'''
statement

while expression:
    statement(s)

'''

i = 1

while True:
    print(i)
    i = i + 1
    if(i > 5):
        break


# for loop

'''
for target in iterable:
    statement

'''

# list comprehension

# [ expression for target in iterable 
#                      lc-clauses ]

# 1 The break Statement

# he break statement is allowed only inside a loop body. When break executes, the loop terminates.

# 2 The continue Statement

# The continue statement is allowed only inside a loop body.
#  When continue executes, the current iteration of the loop body terminates,
#  and execution continues with the next iteration of the loop. 


# 3 The pass Statement

# The body of a Python compound statement cannot be empty—it must contain at least one statement. 
# The pass statement, which performs no action, can be used as a placeholder when a statement is
#  syntactically required but you have nothing specific to do.

for i in 'python':
    if i == 'h':
        pass
        print("this is passed ")    

    print("ele " , i)

# h will be printed


# assert statement ------ >


'''
debugging tool as it brings the programn on halt as soon as any error message is occurred and 
shows on which point of the programn error has occured


                          |---->--- T -->-- programn continues  
code ->-assert condition->-  
                          |---->--- F -->-- assertion stop the programn and gives assertion message
''' 
# synatax 

#  assert <contion> , <error message>

# assertion is raised when condition is false

# n = int(input("enter a number "))

# assert n>10 , "wrong input"

# print("u enterd" , n)


# try/except

'''
try:
    code that might raise exception

except:
    execute this code if there is an exception generated

else:
    if exception is not raised

finally:
    raised no matters, exception is raised or not            

'''


# x = 0

# try:
#     ans = 1/x
    
# except ZeroDivisionError:
#     ans = "not defined"

# print("answer is " , ans)

