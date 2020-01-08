'''

In computing, a process is an instance of a computer program that is being executed. Any process has 3 basic components:

1. An executable program.
2. The associated data needed by the program (variables, work space, buffers, etc.)
3. The execution context of the program (State of process)

A thread is an entity within a process that can be scheduled for execution. 
Also, it is the smallest unit of processing that can be performed in an OS (Operating System).

In simple words, a thread is a sequence of such instructions within a program that can be executed 
independently of other code. For simplicity, you can assume that a thread is simply a subset of a process!

Multithreading is defined as the ability of a processor to execute multiple threads concurrently.

there are 3 ways to impliment threads in python --

1. using function
 t = Thread(target=functionName , args)
 t.start()

2. extend the thread class

class MyThread(Thread)
override the run()
t.start()

3. without extending thread class

class MyThread
display()
t = Thread(target=myobj.display , args)

'''


# Main Thread

'''
import threading

print("current thread " , threading.current_thread().getName())

o/p - current thread  MainThread                                                                                                                

'''

# 1. Thread using function
# create a function to display numbers 0-10, then spon function as thread of own

# creating thread from function

'''
from threading import Thread
import threading

def numbers():
    i = 0
    while(i<10):
        print(i)
        i+=1
    print("curre--"  , threading.current_thread().getName())  # Thread-1   

t = Thread(target=numbers)   # create object to spon/create thread 
t.start()

print("curre--"  , threading.current_thread().getName()) # MainThread


'''


# 2. Create thread class by extending Thread class

# step 1 - import Thread
# step 2 - create class and inherit Thread, 
# step 3 - override run() function


'''

from threading import Thread

class RandomThread(Thread):   # extends Thread
    def run(self):
        i = 0
        while(i<10):
            print(i)
            i+=1

t = RandomThread()   # create object
t.start()            # start
 
'''


# 3. create Thread using class / without extending Thread class




'''
from threading import *

class RandomThread:
    
    def numbers(self):
        i = 0
        while(i<5):
            print(i)
            i += 1
            
obj = RandomThread()    # object, instance of class
t = Thread(target=obj.numbers)
t.start()

'''


# lets see multithreading in action

'''
from threading import *

class RandomThread:
    
    def numbers(self):
        i = 0
        print(current_thread().getName())
        while(i<4):
            print(i)
            i += 1
            
obj = RandomThread()  

t1 = Thread(target=obj.numbers)
t1.start()

t2 = Thread(target=obj.numbers)
t2.start()

t3 = Thread(target=obj.numbers)
t3.start()

# have 3 threads
# output depends on - python thread schedular, so ever time different outputs, bcz of thread scheduling
'''

