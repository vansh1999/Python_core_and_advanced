
import time

starttime = time.perf_counter()

for i in range(1,100):
    if (i == 20 or i == 40):
        print(i , "hell ya")


endtime = time.perf_counter()

print(endtime - starttime)

# output -- 8.3243234e-05 -- exponential - 5 zeros before 8 (time in seconds)