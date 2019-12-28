# Regular expression/Regex
# https://www.w3schools.com/python/python_regex.asp
# bunch of characters or patterns to find a string within string or to validate a given pattern

# Import the re module:
# import re

# RegEx Functions
# The re module offers a set of functions that allows us to search a string for a match:
# re  ----  match , search , findall , split , sub

# findall	Returns a list containing all matches
# search	Returns a Match object if there is a match anywhere in the string
# split	    Returns a list where the string has been split at each match
# sub	    Replaces one or many matches with a string


# sequence characters -- match the patterns

# \d --  any digit(0-9)
# \D -- non digit
# \s -- space , Returns a match where the string contains a white space character	
# \S -- non space
# \w -- Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	
# \W -- Returns a match where the string DOES NOT contain any word characters	
# \b -- space around words , Returns a match where the specified characters are at the beginning or at the end of a word	
# \B -- Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
# \A -- only start of the string
# \Z -- only end of the string


# Metacharacters
# Metacharacters are characters with a special meaning:

# []	A set of characters
# \	Signals a special sequence (can also be used to escape special characters)
# .	Any character (except newline character)
# ^	Starts with
# $	Ends with
# *	Zero or more occurrences
# +	One or more occurrences
# {}	Exactly the specified number of occurrences
# |	Either or
# ()	Capture and group	



# search
# import re

# strf = "The rain in Spain"

# res = re.search(r'r\w+' , strf)

# print(res.group())




# findall
# import re

# strf = "The rain in Spain"
# x = re.findall("ai", strf)
# print(x)




# split()

# import re

# str = "The rain in Spain"
# x = re.split("\s", str)
# print(x)


# sub()

# import re

# str = "The rain in Spain"
# x = re.sub("\s", "9", str)
# print(x)

# import re

# str = "The rain in Spain"
# x = re.sub("\s", "9", str, 2)
# print(x)


# Match -- object

# import re
# str = "The rain in Spain"
# x = re.search("ai", str)
# print(x) #this will print an object


# The Match object has properties and methods used to retrieve information about the search, and the result:

# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match



# import re

# str = "The rain in  Spaaain"
# x = re.search(r"\bS\w+", str)
# print(x.span())


# import re

# str = "The rain in Spain"
# x = re.search(r"\bS\w+", str)
# print(x.string)


# import re

# str = "The Sam rain in Spain"
# x = re.search(r"\bS\w+", str)
# print(x.group())

