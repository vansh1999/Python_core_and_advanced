# application of Threads
from threading import *

class BookBus:
    
    def __init__(self , avaliableSeat):   # class init, avaliable seats
        self.avaliableSeat = avaliableSeat
        self.l = Lock()      # use of lock, while one thread is doing its process , between checking
                            # avaliable seats and reducing seats, it makes sures that that another process
                            # don't enter a book same seats
        
    
    def buy(self , seatRequested):
        self.l.acquire()   # acquire lock
        
        if(self.avaliableSeat >= seatRequested):
            print("Total avaliable seats : " , self.avaliableSeat)
            
            print("loding the ticket")
            print("booking the ticket")
            print("confirming the ticket")
            self.avaliableSeat = self.avaliableSeat - seatRequested
            print("Total avaliable seats : " , self.avaliableSeat)
            
        else:
            print("Sorry no seat avaliable")
            
        self.l.release()     # release lock
        
        


obj = BookBus(10)

t1 = Thread(target=obj.buy , args = (2,))    # take arguments as list
t2 = Thread(target=obj.buy , args = (4,))

t1.start()
t2.start()

