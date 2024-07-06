// const statusDisplay = document.querySelector('.game--status');

// TODO: picture instead of .cell.x and .cell.o in cell when clicked

// var x = document.createElement("img");
// x.src="front-end/assets/x-icon-red-50.png";

// var o = document.createElement("img");
// o.src="front-end/assets/o-icon-50.png";



// let GAME = {
//     X_CLASS : 'x', // value for female // x as oo's
//     Y_CLASS : 'y', // value for male  // y as xx's
//     turn : undefined,
//     winner : null,


//     selectedProfile :  document.querySelectorAll(".id"),
//     blockElement : document.querySelectorAll('[data-cell-index]'),


//     boardElement : document.getElementById("board"),
//     startBtn : document.getElementById("startBtn"),
//     startWindow : document.querySelector(".start-game"),
//     winEl: document.querySelector(".winner-msg"),
//     drawEl : document.querySelector(".draw-msg"),
//     winnerImg : document.querySelector(".winner-msg .winner"),
//     restartBtn : document.getElementById("restartBtn"),
//     drawBtn : document.getElementById("drawBtn"),
// }

// let gameActive = true;
// let currentPlayer = "X";
// let gameState = ["", "", "", "", "", "", "", "", ""];

// // const winningMessage = () => `Player ${currentPlayer} has won!`;
// // const drawMessage = () => `Game ended in a draw!`;
// // const currentPlayerTurn = () => `It's ${currentPlayer}'s turn`;

// // statusDisplay.innerHTML = currentPlayerTurn();

// const winningConditions = [
//     [0, 1, 2],
//     [3, 4, 5],
//     [6, 7, 8],
//     [0, 3, 6],
//     [1, 4, 7],
//     [2, 5, 8],
//     [0, 4, 8],
//     [2, 4, 6]
// ];

// function handleCellPlayed(clickedCell, clickedCellIndex) {
//     gameState[clickedCellIndex] = currentPlayer;
//     clickedCell.innerHTML = currentPlayer;
// }

// function handlePlayerChange() {
//     currentPlayer = currentPlayer === "X" ? "O" : "X";    
//     // statusDisplay.innerHTML = currentPlayerTurn();
// }

// function handleResultValidation() {
//     let roundWon = false;
//     for (let i = 0; i <= 7; i++) {
//         const winCondition = winningConditions[i];
//         let a = gameState[winCondition[0]];
//         let b = gameState[winCondition[1]];
//         let c = gameState[winCondition[2]];
//         if (a === '' || b === '' || c === '') {
//             continue;
//         }
//         if (a === b && b === c) {
//             roundWon = true;
//             break
//         }
//     }

//     if (roundWon) {
//         statusDisplay.innerHTML = winningMessage();
//         gameActive = false;
//         return;
//     }

//     let roundDraw = !gameState.includes("");
//     if (roundDraw) {
//         statusDisplay.innerHTML = drawMessage();
//         gameActive = false;
//         return;
//     }

//     handlePlayerChange();
// }

// function handleCellClick(clickedCellEvent) {
//     const clickedCell = clickedCellEvent.target;
//     const clickedCellIndex = parseInt(clickedCell.getAttribute('data-cell-index'));

//     if (gameState[clickedCellIndex] !== "" || !gameActive) {
//         return;
//     }

//     handleCellPlayed(clickedCell, clickedCellIndex);
//     handleResultValidation();
// }

// function handleRestartGame() {
//     gameActive = true;
//     currentPlayer = "X";
//     gameState = ["", "", "", "", "", "", "", "", ""];
//     statusDisplay.innerHTML = currentPlayerTurn();
//     document.querySelectorAll('.cell').forEach(cell => cell.innerHTML = "");
// }


// document.querySelectorAll('.cell').forEach(cell => cell.addEventListener('click', handleCellClick));
// document.querySelector('.restart-button').addEventListener('click', handleRestartGame);
 


// // handler onclick function of the cell
// function handleClick(e){
//     const cell = e.target;
//     const currentClass = GAME.turn ? GAME.Y_CLASS : GAME.X_CLASS;
//     markCell(cell, currentClass);

//     /** check winner */
//     let flag = checkWin(currentClass, GAME.blockElements).filter((win, index) => {
//        if (win){
        
//         // add green background to the winner 
//         WIN_COMBINATIONS[index].map(i => {
//             GAME.blockElements[i].classList.add('win');
//         })

//         // set the winner
//         GAME.winner = GAME.blockElements[WIN_COMBINATIONS[index][0]].cloneNode(true);
//         return win !== false;
//        }
//     })
// }



// // iterate over cells and add click event
// GAME.blockElement.forEach(cell => {
//     cell.classList.remove(GAME.X_CLASS);
//     cell.classList.remove(GAME.Y_CLASS);
//     cell.classList.remove("win");
//     cell.removeEventListener("click", handleClick);
//     cell.addEventListener('click', handleClick, { once: true })
// })

// GAME.startWindow.classList.add("hide");
// GAME.winEl.classList.remove("show");
// GAME.drawEl.classList.remove("show");
// GAME.winnerImg.children.length ? GAME.winnerImg.removeChild(GAME.winner) : null; 



const X_CLASS = "x";
const O_Class = "o";

function Cell(){
    let selectedCell = document.querySelectorAll(".game-container .game-board .cell");  //querySelectorAll Returns all element descendants of node that match selectors. here it returns all board cells with class=cell //
    selectedCell.forEach(cell=> {   // goes throw all cells 
        // console.log(cell);   // displays all the cells in the browser/website console
        cell.addEventListener("click", e=>{
            let target = e.target.dataset.cell_index; // stores selected/clicked cell index in variable "target"
            // removeCellSelection(selectedCell);
            document.querySelector(`[data-cell_index='${target}']`).classList.add("selected"); // selected/clicked cell "target" will be filled with icon (see css file; /* fills the selected div/cell of game-board with icon */ )
        console.log(e.target.dataset.cell_index); // displays selected/clicked cell index in the browser/website console
        // console.log(target);
        });
    });
}


Cell() 

// TODO: not used/needed yet, it removes selection/icon from cell 
// function removeCellSelection(div){
//     [].forEach.call(div, function(el){
//         el.classList.remove("selected"); 
//     });
// }