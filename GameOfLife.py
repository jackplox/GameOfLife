import random
import os
import time

xDimension = 50
yDimension = 50
chanceOfSpawning = 10
delay = 0.1 #ms Delay time for each frame

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

def RunGame():
	
	iteration = 0
	#print("START")

	gameField = {}

	gameIsOn = True

	while(gameIsOn):
		clear_screen()
		currentString = ""
		nextField = {}
		for i in range(yDimension):
			for j in range(xDimension):
				if iteration == 0:
					#print("I = " + str(i) + "\nJ = " + str(j))
					currentString = initialPrint(j, i, currentString, gameField, chanceOfSpawning)
					continue
				nextField[(j, i)] = evaluateCell(j, i, gameField)
				#print("GAMEFIELD["+ str(j) + ", " + str(i) + "] = " + str(gameField.get((j,i))))
				currentString += nextField[(j, i)]
			currentString += "\n"

		if iteration > 0:
			# if gameField == nextField:
			# 	print(f"Matching cells: {sum(gameField[k] == nextField[k] for k in nextField)}/{len(nextField)}")
			# 	print(f" -- The game of life has ended.\nYour game lasted {Colors.RED}" + str(iteration) + f"{Colors.RESET} iterations.")
			# 	return 0
			gameField=nextField
		
		iteration += 1
		
		print("ITERATION: " + str(iteration))
		print("CURRENT STRING = \n" + currentString)
		

		time.sleep(delay)

def initialPrint(xDimension, yDimension, currentString, gameField, chanceOfSpawning):
	aliveCell = f" {Colors.CYAN}0{Colors.RESET} "
	deadCell = f" {Colors.RED}-{Colors.RESET} "
	
	gameField[(xDimension, yDimension)] = aliveCell if random.randrange(0, 100) <= chanceOfSpawning else deadCell
	currentString += gameField[(xDimension, yDimension)]

	#print("CURRENTSTRING: \n" + currentString)
	return currentString

def evaluateCell(xDimension, yDimension, gameField): 
 
	aliveCell = f" {Colors.CYAN}0{Colors.RESET} "
	deadCell = f" {Colors.RED}-{Colors.RESET} "
	gameIsOn = True
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

	#print("EVALUATING CELL: ( " + str(xDimension) + ", " + str(yDimension) + " ) = " + str(gameField.get((xDimension,yDimension))) + "\nNEIGHBORS: " + str(neighbors))

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
