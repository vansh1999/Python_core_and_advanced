# Threads - real application.

# programn to greet people by name and assign id to them
'''
import time

st = time.perf_counter()

def greet_them(people):
    
    for p in people:
        print("hey " + p + " how are you")
        time.sleep(1)

def assign_id(people):
    
    i = 100;
    for p in people:
        
        print("{} your id is {}".format(p , i))
        i =i +1
        time.sleep(1)

people = ["vansh" , "abc" , "xyz"]



greet_them(people)
assign_id(people)


et = time.perf_counter()
print("execution time is " , et-st)
'''
# You can see the process executed sequentially and we have the total processing time as well which is 6 seconds.


# 2. Python Threading Example

# creating thread using functions


import time
import threading

st = time.perf_counter()

def greet_them(people):
    
    for p in people:
        print("hey " + p + " how are you")
        time.sleep(1)



def assign_id(people):
    
    i = 100;
    for p in people:
        
        print("{} your id is {}".format(p , i))
        i =i +1
        time.sleep(1)

people = ["vansh" , "abc" , "xyzz"]



# creating Threads

t1 = threading.Thread(target = greet_them , args = (people,))
t2 = threading.Thread(target = assign_id , args = (people,))


# start the Thread
t1.start()
t2.start()

# join the Threads
t1.join()   # if we don't join, execution time will be printed after name 1 and id 1.
t2.join()

# use of join() - Your intepreter will stay running until all the threads terminate


et = time.perf_counter()
print("execution time is " , et-st)

# You see this time it didn’t execute sequentially. And the overall execution time is reduced by 50%. So that is why we use Threads.
# execution time is 3.006 seconds


