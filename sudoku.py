# Problem 3

class Solution:
    def isValidSudoku(self, board):
        # creates sets to track the rows and columns
        seen_rows = [set() for _ in range(9)]
        seen_columns = [set() for _ in range(9)]
        seen_boxes = [set() for _ in range(9)]

        # iterate throughout each cell
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    # calculate index 
                    box_index = (i // 3) * 3 + (j // 3)

                    # check duplicates
                    if (num in seen_rows[i] or
                        num in seen_columns[j] or
                        num in seen_boxes[box_index]):
                        return False

                    # mark the box row or column as seen
                    seen_rows[i].add(num)
                    seen_columns[j].add(num)
                    seen_boxes[box_index].add(num)

        return True
    
# Testing
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

board2 = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

# test
solver = Solution()
valid = solver.isValidSudoku(board)
print(valid) # expected true

solver = Solution()
valid = solver.isValidSudoku(board2)
print(valid) # expect false