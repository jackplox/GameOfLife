import random
import os
import time

xDimension = 50
yDimension = 50
chanceOfSpawning = 25
delay = 0.1 #ms Delay time for each frame

class Cell:
    dead = ' \033[91m' + '-' + '\033[0m '  # \033[91m = Red 
    alive = ' \033[96m' + '0' + '\033[0m ' # \033[96m = Cyan
                                           # \033[0m = Reset color

def RunGame():
	
	iteration = 0

	gameField = {}

	gameIsOn = True

	while(gameIsOn):
		ClearScreen()
		currentString = ""
		nextField = {}
		for i in range(yDimension):
			for j in range(xDimension):
				if iteration == 0:
					currentString = InitialPrint(j, i, currentString, gameField, chanceOfSpawning)
					continue
				nextField[(j, i)] = EvaluateCell(j, i, gameField)
				currentString += nextField[(j, i)]
			currentString += "\n"

		if iteration > 0:
			gameField=nextField
		
		iteration += 1
		
		print("ITERATION: " + str(iteration))
		print("CURRENT STRING = \n" + currentString)
		

		time.sleep(delay)

def InitialPrint(xDimension, yDimension, currentString, gameField, chanceOfSpawning):
	
	gameField[(xDimension, yDimension)] = Cell.alive if random.randrange(0, 100) <= chanceOfSpawning else Cell.dead
	currentString += gameField[(xDimension, yDimension)]

	return currentString

def EvaluateCell(xDimension, yDimension, gameField): 
 
	neighbors = 0

	for i in range(3):
		yOffset = i - 1
		for j in range(3):
			xOffset = j - 1
			if xOffset == 0 and yOffset == 0:
				continue
			try:
				if gameField[(xDimension + xOffset, yDimension + yOffset)] == Cell.alive:
					neighbors += 1	
			except:
				# Out of bounds position
				continue

	isAlive = gameField[(xDimension, yDimension)] == Cell.alive
	if isAlive:
		# Check the rules of Conway's Game of Life
	    if neighbors < 2 or neighbors > 3:
	        return Cell.dead
	    else:
	        return Cell.alive
	else:
	    if neighbors == 3:
	        return Cell.alive
	    else:
	        return Cell.dead
			

def ClearScreen():
    # Check the operating system name
    if os.name == 'nt':
        # Command for Windows
        _ = os.system('cls')
    else:
        # Command for Linux, macOS, and others
        _ = os.system('clear')

RunGame()
