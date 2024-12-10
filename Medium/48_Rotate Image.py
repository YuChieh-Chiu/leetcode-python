class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Thought:
        - Problem Description:
            - Rotate the matrix by 90 degrees (clockwise).
            - Do not return anything; modify the matrix in-place instead.
        - Tips:
            - By analyzing the relationship between the input and output in Examples 1 and 2, we observe that after a clockwise rotation, the i-th row of the new matrix is formed by the i-th element of each row in the original matrix.
        - Steps:
            (1) Create a temporary matrix as a reference to maintain the integrity of values during in-place modification.
            (2) Use a loop to construct each row of the matrix based on the observation above.
                - Note. the order in the row should be reversed.
        """
        row = len(matrix)
        col = len(matrix[0])
        tmp_matrix = matrix[:][:]
        for i in range(row):
            matrix[i] = [tmp_matrix[-j-1][i] for j in range(col)]
