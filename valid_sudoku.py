#Question: https://neetcode.io/problems/valid-sudoku/question?list=neetcode150

#Function to calculate the unique sub-boxes
def sub_boxes(board, start_index_i, end_index_i, start_index_j, end_index_j):
        seen_sub_square = set()
        for i in range(start_index_i,end_index_i):
            for j in range(start_index_j,end_index_j):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen_sub_square:
                    return False
                seen_sub_square.add(board[i][j])
        return True

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
    

    #Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not sub_boxes(board, i ,i+3, j, j+3):
                return False
    return True
    
    

#Write the solution in Neetcode way.










#Example Board for testing
board=[["1","2",".",".","3",".",".",".","."],
       ["4",".",".","5",".",".",".",".","."],
       [".","9","1",".",".",".",".",".","3"],
       ["5",".",".",".","6",".",".",".","4"],
       [".",".",".","8",".","3",".",".","5"],
       ["7",".",".",".","2",".",".",".","6"],
       [".",".",".",".",".",".","2",".","."],
       [".",".",".","4","1","9",".",".","8"],
       [".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))