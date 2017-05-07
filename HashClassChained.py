import numpy as np
import math
import List


class ChainedHash:

    def __init__(self, m):
        self.dim=m
        while self.isPrime(self.dim)==False:
            self.dim-=1
        print("dimensione tabella: ",self.dim)
        self.array=np.empty([self.dim,],dtype=List.LinkedList)
        self.fillArray()

    def fillArray(self):
        for i in range(0,self.dim):
            self.array[i]=List.LinkedList()

    def isPrime(self,n):
        if n == 2:
            return True
        if n % 2 == 0 or n <= 1:
            return False
        sqr = int(math.sqrt(n)) + 1
        for divisor in range(3, sqr, 2):
            if n % divisor == 0:
                return False
        return True

    def hash(self,k):
        return k%self.dim

    def insert(self,k):
        self.array[self.hash(k)].add(k)

    def search(self,k):
        for i in range(0,self.dim):
            if self.array[i].search(k):
                return True
        return False

    def delete(self,k):
        self.array[self.hash(k)].remove(k)

    def toString(self):
        for i in range(0,self.dim):
            print(self.array[i].printL(i))

    def getCollisionsNumber(self):
        self.collisionsNumber=0;
        for i in range(0,self.dim):
            if self.array[i].size()!=0:
                self.collisionsNumber+=self.array[i].size() - 1
        return self.collisionsNumber
