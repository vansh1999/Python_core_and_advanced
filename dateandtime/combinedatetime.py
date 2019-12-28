# 1. combine date and time
'''
from datetime import *

d = date(2019 , 12 , 28)

t = time(16 , 20 , 12)

dt = datetime.combine(d,t)
print(dt)
'''

# 2. sorting dates

from datetime import *
import time

ldates = []

d1 = date(2019, 8, 12)
d2 = date(2019, 3, 11)
d3 = date(2019, 3, 12)

ldates.append(d1)
ldates.append(d2)
ldates.append(d3)

ldates.sort()   # default - ascending

print("program started")

for d in ldates:
    print(d)

# 3. sleep program
time.sleep(5)   # program waits for 5 seconds
print("\n end here")


