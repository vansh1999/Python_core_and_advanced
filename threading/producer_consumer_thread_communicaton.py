from threading import *
from time import *

class Producer:
    def __init__(self):
        self.products = []
        self.orderplaced = False


    def produce(self):
        for i in range(1,5):
            self.products.append("product"+str(i))  
            sleep(0.01)
            print("Item Added")
        self.orderplaced = True


class Consumer:
    def __init__(self , prod):
        self.prod   =   prod

    def consume(self):
        while self.prod.orderplaced == False:
            print("Waiting for the order.......")
            sleep(0.2)

        print("orderd ship" , self.prod.products)    

p = Producer()
c = Consumer(p)

t1 = Thread(target= p.produce)
t2 = Thread(target=c.consume)

t1.start()
t2.start()
        