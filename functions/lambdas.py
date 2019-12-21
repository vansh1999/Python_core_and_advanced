# lambdas - way of declaring functions

# --- anonymous function, does'nt have any name

# syntax 

# lambda argument_list : expression

# assign to var and then use it

#  f = lambda x:x*x

# result = f(10)

# use
# 1 filter
# 2 map
# 3 reduce

# find cube of function

# f = lambda x: x**3

# result = f(2)

# print(result)


# print(f(2))


# even - yes , odd -- no


# l = lambda x: 'yes' if x%2==0 else 'no'

# print(l(5))

# cal sum of two numbers

# s = lambda x,y : x+y

# print(s(1,2))


# lets see filter,map & reduce


#1 . filter function

# used to filter the data set
# syntax ---  filter(<lambda fun> , <data-set>)

# lst = [1,2,3,4,5,6,7,8]

# res = list(filter(lambda x: x%2 == 0 , lst))

# print(res)


# 2 . map function

# used to do function in all data set

# double lst value

# lst = [2,5,10]

# f = list(map(lambda x: x*2 , lst))

# print(f)


# reduce - in data set result get reduced.
# to find sum of all numbers/elements in list

# from functools import reduce

# lst = [1,2,5,78,9,1]

# f = reduce(lambda x,y: x+y , lst)

# print(f)


# decorators

# def de(fun):
#     def inn():
#         result = fun()
#         return result*2
#     return inn

# def num():
#     return 5

# resfun = de(num)
# print(resfun())    





