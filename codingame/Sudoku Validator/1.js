let sudoku = [];

for (let i = 0; i < 9; i++) {
    var inputs = readline().split(' ');
    sudoku.push([]);
    for (let j = 0; j < 9; j++) {
        const n = parseInt(inputs[j]);
        sudoku[sudoku.length - 1].push(n);
    }
}

function generateNumberCheckArray() {
    let check = [];
    for (let i = 0; i < 9; i++) {
        check.push(0);
    }
    return check;
}

function checkRows(sudoku) {
    for (let row = 0; row < sudoku.length; row++) {
        let check = generateNumberCheckArray();
        for (let col = 0; col < sudoku[row].length; col++) {
            check[sudoku[row][col] - 1]++;
        }
        for (let num of check) {
            if (num !== 1) {
                return false;
            }
        }
    }
    return true;
}

function checkCols(sudoku) {
    for (let col = 0; col < sudoku.length; col++) {
        let check = generateNumberCheckArray();
        for (let row = 0; row < sudoku.length; row++) {
            check[sudoku[row][col] - 1]++;
        }
        for (let num of check) {
            if (num !== 1) {
                return false;
            }
        }
    }
    return true;
}

function checkSquares(sudoku) {
    for (let col = 0; col < sudoku.length; col += 3) {
        for (let row = 0; row < sudoku.length; row += 3) {
            let check = generateNumberCheckArray();
            for (let i = col; i < col + 3; i++) {
                for (let k = row; k < row + 3; k++) {
                    check[sudoku[i][k] - 1]++;
                }
            }
            for (let num of check) {
                if (num !== 1) {
                    return false;
                }
            }
        }
    }
    return true;
}

if (checkRows(sudoku) && checkCols(sudoku) && checkSquares(sudoku)) {
    console.log('true');
} else {
    console.log('false');
}
