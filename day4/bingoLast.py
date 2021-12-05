import numpy as np

def loadFile(fileName):
    listBoard = []
    listNums = []
    ln = 0
    tempList = []
    with open(fileName) as fh:
        for line in fh:
            if (ln==0):
                listNums = list(map(int,line.split(',')))
            elif ((ln-1)%6==0 and ln>1): #Skip line 1, because temp is empty
                listBoard.append(tempList)
                tempList = []
            elif ((ln-1)%6!=0): # If there's text append to partial board
                parsedLine = line.split(' ')
                parsedLine = [t for t in parsedLine if t!=''] # Remove extra spaces
                tempList.append(list(map(int, parsedLine)))
            ln += 1

    listBoard.append(tempList) # The last board isn't appended bc there's no extra empty line

    return listBoard, listNums

###

checkBingo = lambda x: (True in np.all(x, axis=1)) or (True in np.all(x,axis=0))
xorFunc = lambda x,y: x ^ y

listBoard, listNums = loadFile('input.txt')
listBoard = np.array(listBoard)
listChecks = np.zeros(listBoard.shape)==True # array to keep track of bingos
bingoList = list(map(checkBingo, listChecks)) # initialize

for num in listNums:
    bingoList_previous = bingoList.copy()
    listChecks |= (listBoard==num) # Update check board with new number
    bingoList = list(map(checkBingo, listChecks))
    change = list(map(xorFunc, bingoList, bingoList_previous)) # the last that changed
    if True in change:
        winningNum = num
        winningBoard = np.squeeze( listBoard[change] )
        winningChecks = np.squeeze( listChecks[change] )

scoreUnmarked = np.sum( winningBoard[winningChecks==False] )
scoreTotal = scoreUnmarked * winningNum

print(scoreUnmarked, winningNum, scoreTotal)

# Another way to check if the bingo list has changed is comparing sums (the number of True's changes is the number of bingos changes. Using the current method one already has the index list for later, though.
