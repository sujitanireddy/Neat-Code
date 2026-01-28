#Question: https://neetcode.io/problems/valid-sudoku/question?list=neetcode150

def isValidSudoku(board: list[list[str]]) -> bool:

    #Not a valid board
    if len(board) != 9:
        return False
    
    #Each row must contain the digits 1-9 without duplicates.

    for row in board:
        seen = set()
        for num in row:
            if num == ".":
                continue
            if num in seen:
                return False
            seen.add(num)
        #print(seen)
    
    #Each column must contain the digits 1-9 without duplicates

    for i in range(len(board)):
        seen_column = set()
        for j in range(len(board[i])):
            if board[j][i] == ".":
                continue
            if board[j][i] in seen_column:
                return False
            seen_column.add(board[j][i])
        #print(seen_column)
    

    #Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.


    
    
    


























board =[["1","2",".",".","3",".",".",".","."],
        ["4",".",".","5",".",".",".",".","."],
        [".","9","8",".",".",".",".",".","3"],
        ["5",".",".",".","6",".",".",".","4"],
        [".",".",".","8",".","3",".",".","5"],
        ["7",".",".",".","2",".",".",".","6"],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","4","1","9",".",".","8"],
        [".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))