document.addEventListener("DOMContentLoaded", () => {
    var background = document.createElement("DIV");
    background.setAttribute("id", "bg");

    var bgPara = document.createElement("P");
    bgPara.setAttribute("id", "game");
    var bgText = document.createTextNode("");

    bgPara.appendChild(bgText)
    background.appendChild(bgPara);


    let xDimension = 50;
    let yDimension = 50;
    let chanceOfSpawning = 50;
    let delay = 100; // milliseconds
    let gameField = {};


    //Initialize field
    for (let i = 0; i < yDimension; i++) {
        for (let j = 0; j < xDimension; j++) {
            let cellPos = j.toString() + "," + i.toString();
            gameField[cellPos] = (Math.floor(Math.random() * 100)) < chanceOfSpawning ? " 0 " : "   ";
        }
    }

    const gameLoop = setInterval(() => {
        let currentString = "";
        let nextField = {};

        for (let i = 0; i < yDimension; i++) {
            for (let j = 0; j < xDimension; j++) {
                let cellPos = j.toString() + "," + i.toString();
                nextField[cellPos] = EvaluateCell(j, i, gameField);
                currentString += nextField[cellPos];
            }
            currentString += "\n";
        }

        gameField = nextField;
        
        bgText.textContent = currentString;// Writing the field

    }, delay);

    function EvaluateCell(xPos, yPos, gameField) {
        let aliveCell = " 0 ";
        let deadCell = "   ";
        let neighbors = 0;

        for (let i = 0; i < 3; i++) {
            let yOffset = i - 1;
            for (let j = 0; j < 3; j++) {
                let xOffset = j - 1;
                if (xOffset == 0 && yOffset == 0) continue;

                let cellPos = (xPos + xOffset).toString() + "," + (yPos + yOffset).toString();
                if (gameField[cellPos] == aliveCell) {
                    neighbors += 1;
                }
            }
        }

        let cellPos = xPos.toString() + "," + yPos.toString();
        let isAlive = gameField[cellPos] == aliveCell;

        if (isAlive) {
            return (neighbors < 2 || neighbors > 3) ? deadCell : aliveCell;
        } else {
            return neighbors == 3 ? aliveCell : deadCell;
        }
    }

    document.body.appendChild(background);
});