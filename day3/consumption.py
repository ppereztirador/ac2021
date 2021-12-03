import numpy as np

listValues = []
with open('input') as fh:
    for line in fh:
        listValues.append(list(map(int,line[:-1]))) # -1 to skip \n

listValues = np.array(listValues)

# If the sum of each column > half then '1' is more common
halfValue = int(listValues.shape[0])/2
sumValues = np.sum(listValues, axis=0)

bitConversion = 2 ** np.arange(listValues.shape[1]-1, -1, -1)

gamma = sumValues>=halfValue
epsilon = sumValues<halfValue

gammaInt = np.sum(gamma * bitConversion)
epsilonInt = np.sum(epsilon * bitConversion)

print(gammaInt, epsilonInt, gammaInt*epsilonInt)
