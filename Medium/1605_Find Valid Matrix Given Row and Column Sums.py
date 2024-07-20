import numpy as np
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        """
        thought:
        - our goal is to find a 2D matrix where all values are greater than or equal to 0 and satisfy the given `rowSum` and `colSum` requirements.
        - according to the hint provided by LeetCode, we know that by iterating over each position `i` in the matrix and setting the value at that position to `x = min(rowSum[i], colSum[i])`, and then subtracting `x` from both `rowSum[i]` and `colSum[i]`, we can repeat this process until all `rowSum` and `colSum` values equal 0, obtaining the desired matrix.
        - note: The reason this works is due to the constraint in the problem that `sum(rowSum) == sum(colSum)`, which ensures that each row (column) will be less than or equal to the sum of all columns (rows). Therefore, when we zero out a row (column), we reduce the matrix to a smaller one with one less row (column). Repeating this process will eventually lead to a 1x1 matrix, filling all values and making all `rowSum` and `colSum` values equal to 0, satisfying the conditions of the problem.
        - therefore, we can follow these steps:
            (1) first, create a matrix of size `len(rowSum) x len(colSum)` with all positions set to 0
            (2) iterate over each position, setting the value to `x = min(rowSum[i], colSum[i])`, and update `rowSum[i]` and `colSum[i]` to `rowSum[i] - x` and `colSum[i] - x`.
            (3) obtain the resulting matrix.
        """
        len_r, len_c = len(rowSum), len(colSum)
        matrix = np.zeros((len_r, len_c), "i") # "i": integer
        for row in range(len_r):
            for col in range(len_c):
                x = min(rowSum[row], colSum[col])
                matrix[row][col] = x
                rowSum[row] -= x
                colSum[col] -= x
        return matrix.tolist() # although directly returning `matrix` is also correct, since the required return type is `List[List[int]]`, we use `tolist()` here to match the specified format
