# declare a list

lan = ['python' , 'c++' , 'R']

nums = ['one' , 2 ,3 , (4,5)]

# access a list

print(lan[2])

# indexing

print(lan[:])
print(lan[::-1])
print(lan[-1:-4:-1])

# mutable and reassigning

lan[2] = "js"

print(lan)

nums = ['zero' , 0 , 0]

print(nums)



# multiply


nums1 = nums*3
print(nums1)

# length
print(len(nums1))

# METHODS to ADD and REMOVE elements in list

# add at last - use .append()

lan.append("java") # add at lat
print(lan)

# add at index insert - to add at specific index
lan.insert(3,10)


# remove - remove()
lan.remove("python") # removes python from list , use del if want specific index or complete list
print(lan)

# delete a element or entire list

del lan[2]

print(lan)


# del nums

print(nums)

# .clear() METHOD - empty the list

lan.clear()

print(lan)

# max() METHOD - maximun element in list

numbers = [2,4,5]

print(max(numbers))
# print(max(nums))

print(min(numbers))

# sort a list - .sort() <--- method 

numbers.sort()
print(numbers)

# reverse sort method

numbers.sort(reverse=True)
print(numbers)

# sort - sorted() <-- function (inbuild)

print(sorted(numbers))



