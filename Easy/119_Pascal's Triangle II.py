class Solution:
    def increment(self, last_row: List[int]) -> List[int]:

        this_row = [1]

        for i in range(len(last_row)-1):
            this_row.append(last_row[i]+last_row[i+1])

        this_row.append(1)
        
        return this_row
    def getRow(self, rowIndex: int) -> List[int]:
        """
        Thought:
        - Problem description:
            - Return the `rowIndex` row of Pascal's triangle.
            - The row index starts at 0.
        - Idea:
            - Observe the following examples to deduce the pattern:
                (1) rowIndex = 0: [1]
                (2) rowIndex = 1: [1, 1]
                (3) rowIndex = 2: [1, 2, 1]
                (4) rowIndex = 3: [1, 3, 3, 1]
                (5) rowIndex = 4: [1, 4, 6, 4, 1]
            - Pattern:
                (1) When `rowIndex = 0`, the output is [1].
                (2) When `rowIndex = 1`, the output is [1, 1].
                (3) When `rowIndex > 1`, the output is [1, middle values, 1], where the middle values are calculated as the sum of adjacent numbers from the previous row.
        - Steps:
            1. If `rowIndex = 0`, return [1] directly.
            2. If `rowIndex = 1`, return [1, 1] directly.
            3. If `rowIndex > 1`:
                (1) Initialize a variable `last_row` with the values of the previous row, starting as [1, 1].
                (2) Define a function `increment` to compute the middle values by summing adjacent numbers from `last_row`.
                (3) Use a loop to repeatedly call `increment` until the desired row is reached.
        """

        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        
        last_row = [1,1]
        for i in range(rowIndex-1):
            last_row = self.increment(last_row)
        
        return last_row
