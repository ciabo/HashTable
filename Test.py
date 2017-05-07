import pickle
import numpy as np
import random
import HashClassOpen as ho
import HashClassChained as hc

def test():
    val=pickle.load(open("testVal.p","rb"))
    chainedResult=chainedHashTest(val)
    openResult=openHashTest(val)

    pickle.dump(chainedResult,open("chainedResult.p","wb"))
    pickle.dump(openResult, open("openResult.p", "wb"))

def chainedHashTest(val):
    dim = val[0]
    percentage = val[1]
    finalCollisions = []
    collisionsArray = []

    for percent in percentage:
        for i in range(0, 20):
            values = random.sample(range(100 * dim), dim * percent // 100)
            chainedHashTable = hc.ChainedHash(dim)
            for value in values:
                chainedHashTable.insert(value)

            collisionsArray.append(chainedHashTable.getCollisionsNumber())

        maxCollisionsValue = max(collisionsArray)
        minCollisionsValue = min(collisionsArray)
        avgCollisionsValue = sum(collisionsArray) / len(collisionsArray)
        cList = [maxCollisionsValue, minCollisionsValue, avgCollisionsValue]

        finalCollisions.append(cList)
        collisionsArray = []

    return finalCollisions

def openHashTest(val):
    dim=val[0]
    percentage=val[1]
    finalCollisions=[]
    finalInspection=[]
    collisionsArray=[]
    inspectionArray=[]
    for percent in percentage:
        for i in range(0,20):
            openHashTable = ho.HashOpen(dim)
            values = random.sample(range(100*dim), dim * percent // 100)

            for value in values:
                openHashTable.insert(value)

            collisionsArray.append(openHashTable.getCollisionsNumber())
            inspectionArray.append(openHashTable.getIspectionNumbersArray())

        maxCollisionsValue=max(collisionsArray)
        minCollisionsValue=min(collisionsArray)
        avgCollisionsValue=sum(collisionsArray)/len(collisionsArray)
        cList=[maxCollisionsValue,minCollisionsValue,avgCollisionsValue]

        maxInspectionValue = max(max(v) for v in inspectionArray)
        minInspectionValue = min(min(v) for v in inspectionArray)
        avgInspectionValue = sum(sum(v)/len(v) for v in inspectionArray)/len(inspectionArray)
        iList=[maxInspectionValue,minInspectionValue,avgInspectionValue]

        finalCollisions.append(cList)
        finalInspection.append(iList)

        collisionsArray=[]
        inspectionArray=[]

    return finalCollisions,finalInspection

