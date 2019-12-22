# open
#  f = open("file name" , "mode" , "buffer")

# close
# f.close()

'''

Modes

1. w - delete previous and start writing new

2. r - read file from start to end

3. a - append the file, means previous content will not be deleted and new can be added

4. w+ - write + read

5 r+ - read + write + append

6 a+ - append + read

7. x - create new file excusive



'''


# 1. writing a string to file

# open the file for writing

# f = open("firstfile.txt", "w")

# s = input("Enter the text: ")
# writing in file
# f.write(s)

# close the file
# f.close()

# 2. append to previous file

# f = open("firstfile.txt" , "a")
# a = input("ebter text to append ")
# f.write(a)
# f.close()

# 3. read from file

# f = open("firstfile.txt" , "r")
# s = f.read()
# print(s)
# f.close()

# 4. 