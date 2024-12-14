class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Thought:
        - Problem Description:
            - Given an m x n matrix, if an element is 0, set its entire row and column to 0.
            - The function should modify the matrix in-place without returning anything.
        - Follow-Up Approaches:
            - O(mn) space: Use a temporary matrix as a reference to identify rows and columns that need to be set to 0.
            - O(m + n) space: Traverse the matrix to track which rows and columns contain 0, using this information as a reference for modification.
        - Chosen Solution:
            - As suggested in Hint 3, we use the first row that contains a 0 as a tracker to record the columns that need to be set to 0.
            - This approach allows us to achieve constant space complexity.
        - Steps:
            (1) Initialize the first row of the matrix (m_tracker) as a tracker to mark the columns that need to be set to 0.
            (2) Traverse the matrix:
                - For each row, if a cell contains 0, set all cells in that row to 0.
                - Simultaneously, mark the corresponding column in the m_tracker row.
            (3) Using the m_tracker row as a reference, set all cells in the marked columns to 0.
            (4) Finally, set all cells in the m_tracker row to 0.
        """
        m_tracker = -1
        set_to_zero = False # to check whether the row m should be set to 0
        total_m = len(matrix)
        total_n = len(matrix[0])
        for m in range(total_m):
            for n in range(total_n):
                if matrix[m][n] == 0:
                    if m_tracker == -1:
                        m_tracker = m
                        break
                    else:
                        matrix[m_tracker][n] = 0
                        set_to_zero = True
            if set_to_zero:
                matrix[m] = [0] * total_n
                set_to_zero = False
        for n in range(total_n):
            if matrix[m_tracker][n] == 0:
                for i, row in enumerate(matrix):
                    row[n] = 0
        if m_tracker != -1:
            matrix[m_tracker] = [0] * total_n
