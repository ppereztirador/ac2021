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

listBoard, listNums = loadFile('input.txt')
listBoard = np.array(listBoard)
listChecks = np.zeros(listBoard.shape)==True # array to keep track of bingos

for num in listNums:
    listChecks |= (listBoard==num) # Update check board with new number
    bingoList = list(map(checkBingo, listChecks))
    
    if True in bingoList: # if any bingo
        break

winningBoard = np.squeeze( listBoard[bingoList] )
winningChecks = np.squeeze( listChecks[bingoList] )
scoreUnmarked = np.sum( winningBoard[winningChecks==False] )
scoreTotal = scoreUnmarked * num

print(scoreUnmarked, num, scoreTotal)
