class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        thought:
        - Our goal is to build a Pascal's triangle with `numRows` levels.
        - Take a 5-level Pascal's triangle as an example:
            - Level 1: [1]
            - Level 2: [1, 1]
            - Level 3: [1, 2, 1] -> 2 = 1 + 1
            - Level 4: [1, 3, 3, 1] -> 3 = 1 + 2 = 2 + 1
            - Level 5: [1, 4, 6, 4, 1] -> 4 = 1 + 3 = 3 + 1, 6 = 3 + 3
        - Based on the example above, we can derive the following information:
            - Level 1 and Level 2 are always [1] and [1, 1], respectively.
            - For level i greater than 2, the row starts and ends with 1. The internal values are obtained by adding two consecutive values from the previous row. Specifically, the value at index j in level i is the sum of the values at indices j-1 and j in level i-1.
        - Therefore, we can follow these steps:
            1. Initialize a list `pascal` to store the values of Pascal's triangle.
            2. Iterate over each row in the range of `numRows`:
                - If the row index is 0, append [1] to `pascal`.
                - If the row index is 1, append [1, 1] to `pascal`.
                - If the row index is greater than 1, traverse the list `pascal[row-1]` and add two consecutive values to construct `pascal[row]`.
            3. Return the list `pascal`.
        - Note: The above strategy uses dynamic programming (DP) by building each row based on the previous row.
        """
        pascal = []
        for row in range(numRows):
            if row == 0:
                pascal.append([1])
            elif row == 1:
                pascal.append([1,1])
            else:
                row_list = [1]
                for i in range(row-1):
                    row_list.append(pascal[-1][i] + pascal[-1][i+1])
                row_list.append(1)
                pascal.append(row_list)
        return pascal
