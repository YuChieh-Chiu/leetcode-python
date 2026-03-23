class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        """
        Thought:
        - Goal: Find the maximum non-negative product of all integers along a path from (0, 0) to (m-1, n-1).
        - Idea: Use Dynamic Programming to track both the maximum and minimum products at each cell. 
                Tracking the minimum is crucial because a very small negative number multiplied by 
                another negative number can become a large positive maximum.
        - Steps:
            1. Initialize two 1D arrays, dp_max and dp_min, to represent the current row's products (Space Optimization).
            2. Iterate through the grid row by row, then column by column.
            3. Handle the base case (origin), the first row (only from left), and the first column (only from top).
            4. For internal cells, compute four potential values using the max/min of the cell above and the cell to the left.
            5. Update the current dp_max and dp_min values.
            6. Return the maximum product mod 10^9 + 7 if it's non-negative, otherwise return -1.
        - Time Complexity: O(m * n)
        - Space Complexity: O(n)
        """
        rows, cols = len(grid), len(grid[0])
        dp_max = [0]*cols
        dp_min = [0]*cols
        MOD = 10**9 + 7

        for i in range(rows):
            for j in range(cols):
                val = grid[i][j]
                if i == 0 and j == 0:
                    dp_max[j] = dp_min[j] = val
                elif i == 0:
                    dp_max[j] = dp_min[j] = dp_max[j-1] * val
                elif j == 0:
                    dp_max[j] = dp_min[j] = dp_max[j] * val
                else:
                    candidates = (
                        dp_max[j-1] * val,
                        dp_min[j-1] * val,
                        dp_max[j] * val,
                        dp_min[j] * val
                    )
                    dp_max[j] = max(candidates)
                    dp_min[j] = min(candidates)

        res = dp_max[-1]
        return res % MOD if res >= 0 else -1
