// sudoku = [1,2,3,4,5,6,7,8,]

// def hasDuplicate(sudoku):
//     seen = {}
//     for num in sudoku:
//         if num in '123456789':
//             if num in seen: return True
//             else: seen[num] = True
//     return False

// hasDuplicate(sudoku)

const sudoku = [
  [1, 2, 3, 4, 5, 6, 7, 8, 9],
  [2, 3, 4, 5, 6, 7, 8, 9, 1],
  [3, 4, 5, 6, 7, 8, 9, 1, 2],
  [4, 5, 6, 7, 8, 9, 1, 2, 3],
  [5, 6, 7, 8, 9, 1, 2, 3, 4],
  [6, 7, 8, 9, 1, 2, 3, 4, 5],
  [7, 8, 9, 1, 2, 3, 4, 5, 6],
  [8, 9, 1, 2, 3, 4, 5, 6, 7],
  [9, 1, 2, 3, 4, 5, 6, 7, 8],
];

const board = [
  [".", ".", ".", ".", "5", ".", ".", "1", "."],
  [".", "4", ".", "3", ".", ".", ".", ".", "."],
  [".", ".", ".", ".", ".", "3", ".", ".", "1"],
  ["8", ".", ".", ".", ".", ".", ".", "2", "."],
  [".", ".", "2", ".", "7", ".", ".", ".", "."],
  [".", "1", "5", ".", ".", ".", ".", ".", "."],
  [".", ".", ".", ".", ".", "2", ".", ".", "."],
  [".", "2", ".", "9", ".", ".", ".", ".", "."],
  [".", ".", "4", ".", ".", ".", ".", ".", "."],
];

function hasDuplicate(arr) {
  const seen = {};
  for (num of arr) {
    if ("123456789".includes(num)) {
      if (num in seen) return true;
      else seen[num] = true;
    }
  }
  return false;
}

function isValidSudoku(board) {
  // i first check the rows
  for (row of board) {
    if (hasDuplicate(row)) return false;
  }

  //  then i check the columns (this is the tricky part lol)
  //   first i create an array of all the columns, i'm using a nested loop cause it's limited to just 9 rows so it can't be too bad right?
  const columns = [];
  for (row of board) {
    let i = 0;
    for (num of row) {
      if (columns[i]) {
        columns[i].push(num);
        i++;
      } else {
        columns[i] = [num];
        i++;
      }
    }
  }

  //   now i check if there's a duplicate in any of the arrays

  for (col of columns) {
    if (hasDuplicate(col)) return false;
  }
  // now i build the box too
  const boxes = [[], [], [], [], [], [], [], [], []];

  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[i].length; j++) {
      if (j >= 0 && j <= 2) {
        if (i <= 2) {
          boxes[0].push(board[i][j]);
        } else if (i > 2 && i <= 5) {
          boxes[3].push(board[i][j]);
        } else if (i > 5) {
          boxes[6].push(board[i][j]);
        }
      } else if (j >= 3 && j <= 5) {
        if (i <= 2) {
          boxes[1].push(board[i][j]);
        } else if (i > 2 && i <= 5) {
          boxes[4].push(board[i][j]);
        } else if (i > 5) {
          boxes[7].push(board[i][j]);
        }
      } else if (j > 5) {
        if (i <= 2) {
          boxes[2].push(board[i][j]);
        } else if (i > 2 && i <= 5) {
          boxes[5].push(board[i][j]);
        } else if (i > 5) {
          boxes[8].push(board[i][j]);
        }
      }
    }
  }
  //   and i check or duplicates in the boxes

  for (box of boxes) {
    if (hasDuplicate(box)) return false;
  }

  return true;
}

console.log(isValidSudoku(board));
