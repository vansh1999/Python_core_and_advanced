# declare method 1
mydi = {
    1 : "one", # < -- 1
    2 : "two", # <-- 2
    "three" : 3 # <-- 3
}

print(mydi)

print(mydi[1])
print(mydi[2])

# get key() and values()
print(mydi.keys())
print(mydi.values())
print(mydi.items()) # < -- print all the items

# clear the dictionary

# mydi.clear()
# print(mydi)

# delete from dictionary
del mydi[1]
print(mydi)

# mydi.remove(2)
# print(mydi) < -- no remove



# declaring dictionary method - 2
# use dict()


a = dict({101 : "pizza" , 102 : "burger" , 103 : "roti"})

# print(a[0]) < -- error , as starts from 1

print(a)