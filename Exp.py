import pickle
import Test
import matplotlib.pyplot as mp

dim=1000
percentage=(10, 20, 30, 40, 50, 60, 70, 75, 80, 85, 87, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100)
testVal=(dim,percentage)

pickle.dump(testVal, open("testVal.p","wb"))

Test.test()

chainedResults = pickle.load(open("chainedResult.p", "rb"))
openResults = pickle.load(open("openResult.p", "rb"))
openCollisions = openResults[0]
openInspections = openResults[1]

#Plot collisions for chained hash
xAxis = percentage
yMax = [item[0] for item in chainedResults]
yMin = [item[1] for item in chainedResults]
yAvg = [item[2] for item in chainedResults]

mp.plot(xAxis, yMin)
mp.plot(xAxis, yAvg)
mp.plot(xAxis, yMax)

mp.xlabel('Elements percentage')
mp.ylabel('Number of collisions')
mp.legend(['Min', 'Avg', 'Max'], loc=2)
mp.title("Chained Hash Table Collisions")
mp.show()

# Plot collisions for open hash
yMax = [item[0] for item in openCollisions]
yMin = [item[1] for item in openCollisions]
yAvg = [item[2] for item in openCollisions]

mp.plot(xAxis, yMin)
mp.plot(xAxis, yAvg)
mp.plot(xAxis, yMax)

mp.xlabel('Elements percentage')
mp.ylabel('Number of collisions')
mp.legend(['Min', 'Avg', 'Max'], loc=2)
mp.title("Open Hash Table Collisions")
mp.show()

# Plot inspections for open hash
yMax = [item[0] for item in openInspections]
yMin = [item[1] for item in openInspections]
yAvg = [item[2] for item in openInspections]

mp.plot(xAxis, yMin)
mp.plot(xAxis, yAvg)
mp.plot(xAxis, yMax)

mp.xlabel('Elements percentage')
mp.ylabel('Number of inspections')
mp.legend(['Min', 'Avg', 'Max'], loc=2)
mp.title("Open Hash Table Ispections")
mp.show()
