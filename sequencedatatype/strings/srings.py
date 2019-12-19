
s1 = "helo"
s2 = """ 

hi  my 
   name  is 

      vansh

"""

print(s1,s2)

# index
print(s1[0])

# multiply
print(s1*2)


# length
print(len(s1))

# slice 
print(s1[1:4])

s3 = "  you are awer    "
# strip
# removes space from start and end of string
print(len(s3))

stp = s3.strip()
print(len(stp))

# lstrip() , rstrip()

# .find() < - find the index of substring

print(s3.find("are"))

# .find("ele" , start , end)

print(s3.find("are" , 7 , len(s3)))


# .count("ele") <--- count elements in string

print(s3.count("a"))


# .replace("old ele" , "new ele")

print(s3.replace('a' , 'x'))

# .upper() , .lower() --> converts to capital and small letters

