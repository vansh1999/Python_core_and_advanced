#  Generators -- 

# Generators are functions that returns sequence of values back

# generators is 'return' just like any other function but it uses 'yeild' to return back


# Generator-Function : 
# A generator-function is defined like a normal function, 
# but whenever it needs to generate a value, it does so with 
# the yield keyword rather than return. 
# If the body of a def contains yield, the function automatically becomes a generator function.


def cust(x,y):
    while x < y:
        yield x         # store x in memory
        x +=1 

result = cust(10,18)

for i in result:
    print(i)

