# date and time 
# epoch --- 1st Jan 1970 --- start of time in seconds

# ctime() -- time
# datetime -- datetime


# 1  time science epoch

import time  # import time module

epochtime = time.time()  # time() method to get current time

print(epochtime)

# 2 get current time and date in format

t = time.ctime(epochtime)
print(t)

# 3 get current date and time
import datetime
dt = datetime.datetime.today()
print(dt)


print(dt.day , dt.month , dt.year)
print(dt.hour , dt.minute , dt.second)