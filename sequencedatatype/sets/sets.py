
# declare set

set1 = {1,3,4,3}
print(set1)

# index

# print(set1[2]) < -- error -- TypeError: 'set' object does not support indexing

# deleting set
# del set1

# print(set1)


# append

# set1.append(100)
# print(set1) < -- error

# update -- to add in the set
print(set1.update([100]))


# remove
# set1.remove(3)
print(set1)

# pop <-- In set removes the random element and returns the removed element
print(set1.pop())
print(set1)


# slicing

# print(set1[1:2]) 
# error - > TypeError: 'set' object is not subscriptable

# list to set
print("======================")
lst = [10,10,20,20,30,30]
print(lst)
print(type(lst))
st = set(lst)
print(st)
print(type(st))

