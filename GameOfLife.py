import random
import os
import time

xDimension = 50
yDimension = 50
chanceOfSpawning = 25
delay = 0.1 #ms Delay time for each frame

class Colors:
    RED = '\033[91m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

def RunGame():
	
	iteration = 0

	gameField = {}

	gameIsOn = True

	while(gameIsOn):
		clear_screen()
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
	aliveCell = f" {Colors.CYAN}0{Colors.RESET} "
	deadCell = f" {Colors.RED}-{Colors.RESET} "
	
	gameField[(xDimension, yDimension)] = aliveCell if random.randrange(0, 100) <= chanceOfSpawning else deadCell
	currentString += gameField[(xDimension, yDimension)]

	return currentString

def EvaluateCell(xDimension, yDimension, gameField): 
 
	aliveCell = f" {Colors.CYAN}0{Colors.RESET} "
	deadCell = f" {Colors.RED}-{Colors.RESET} "
	neighbors = 0

	for i in range(3):
		yOffset = i - 1
		for j in range(3):
			xOffset = j - 1
			if xOffset == 0 and yOffset == 0:
				continue
			try:
				if gameField[(xDimension + xOffset, yDimension + yOffset)] == aliveCell:
					neighbors += 1	
			except:
				# Out of bounds position
				continue

	isAlive = gameField[(xDimension, yDimension)] == aliveCell
	if isAlive:
	    if neighbors < 2 or neighbors > 3:
	        return deadCell
	    else:
	        return aliveCell
	else:
	    if neighbors == 3:
	        return aliveCell
	    else:
	        return deadCell
			

def clear_screen():
    # Check the operating system name
    if os.name == 'nt':
        # Command for Windows
        _ = os.system('cls')
    else:
        # Command for Linux, macOS, and others
        _ = os.system('clear')

RunGame()
