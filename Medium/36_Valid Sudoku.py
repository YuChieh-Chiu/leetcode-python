class Solution:
    def checkRow(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = board[i]
            if (9 - row.count("."))+1 != len(set(row)):
                return False
        return True
    def checkColumn(self, board: List[List[str]]) -> bool:
        for i in range(9):
            col = [row[i] for row in board]
            if (9 - col.count("."))+1 != len(set(col)):
                return False
        return True
    def checkSubbox(self, board: List[List[str]]) -> bool:
        for i in [0,3,6]:
            for j in [0,3,6]:
                subbox = board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3]
                if (9 - subbox.count("."))+1 != len(set(subbox)):
                    return False
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        thought:
        - our goal is to determine if a 9x9 Sudoku board is valid, based on the following rules:
            (1) each row must contain the digits 1-9 without repetition.
            (2) each column must contain the digits 1-9 without repetition.
            (3) each 3x3 subgrid must contain the digits 1-9 without repetition.
        - to achieve this, we can follow these steps:
            (1) check each row (`board[i]`) to ensure there are no duplicate values.
            (2) check each column (`board[i][j]`) to ensure there are no duplicate values.
            (3) check each 3x3 subgrid to ensure there are no duplicate values.
            (4) if no duplicates are found in any of the steps above, the board is valid; otherwise, it is not.
        """
        if not self.checkRow(board):
            return False
        if not self.checkColumn(board):
            return False
        if not self.checkSubbox(board):
            return False
        return True
