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
