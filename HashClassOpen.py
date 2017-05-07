import numpy as np
import math

class HashOpen:
    # -2 --> empty slot  -1 --> DEL slot
    def __init__(self, m):
        self.dim=m
        while self.isPrime(self.dim)==False:
            self.dim+=1
        print("dimensione tabella: ",self.dim)
        self.array=np.empty([self.dim,])
        self.fillArray()
        self.collisionsNumber=0
        self.ispectionNumbersArray=[]

    def fillArray(self):
        for i in range(0,self.dim):
            self.array[i]=-2 # -2 means empty

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

    def hash(self,k,i):
        return ((k%self.dim)+i)%self.dim

    #try to insert the element in the hash table. Returns the posizione where the elem. has been stored or -10 if the isn't enough space
    def insert(self,k):
        i=0
        while i!= self.dim:
            j=self.hash(k,i)
            if self.array[j] == -2 or self.array[j]==-1:
                self.array[j]=k
                self.ispectionNumbersArray.append(i)
                return j
            else:
                i+=1
                self.collisionsNumber+=1
        return -10

    #search returns the position of the elements or -10 if the element is not found
    def search(self,k):
        i=0
        while i!=self.dim:
            j=self.hash(k,i)
            if self.array[j]==k:
                return j
            elif self.array==-2:
                return -10
            else:
                i+=1
        return -10


    def delete(self,k):
        position=self.search(k)
        if position>=0:
            self.array[position]=-1

    def toString(self):
        print(self.array)

    def getCollisionsNumber(self):
        return self.collisionsNumber

    def getIspectionNumbersArray(self):
        return self.ispectionNumbersArray