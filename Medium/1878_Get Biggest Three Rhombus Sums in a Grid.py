import heapq

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        """
        Thought:
        - Goal: Find the three largest unique rhombus sums in a grid, where a sum includes only the border elements.
        - Idea: For each cell (r, c), consider it as the center. Expand with radius 'q' as long as the four vertices remain within the grid.
        - Steps:
            1. Initialize a set to store unique rhombus sums.
            2. Iterate through each cell (r, c) as the potential center.
            3. Iterate through radius q >= 0.
            4. If q = 0, the sum is the cell itself.
            5. If q > 0, use a loop (i from 0 to q-1) to traverse the four slanted edges:
            - North-East, East-South, South-West, and West-North.
            6. Use heapq.nlargest to efficiently retrieve the top 3 unique sums.
        - Time Complexity: O(m * n * min(m, n)^2) - due to the four nested loops (r, c, q, and the edge traversal).
        - Space Complexity: O(m * n * min(m, n)) - to store all unique sums in the worst case.
        """
        rows = len(grid)
        cols = len(grid[0])
        rhombus = set()
        for r in range(rows):
            for c in range(cols):
                for q in range(min(r, c, rows-r-1, cols-c-1) + 1):
                    if q == 0:
                        rhombus.add(grid[r][c])
                    else:
                        rhombus_sum = 0
                        for i in range(q):
                            rhombus_sum += (
                                grid[r-q+i][c+i] + grid[r+i][c+q-i] + grid[r+q-i][c-i] + grid[r-i][c-q+i]
                            )
                        rhombus.add(rhombus_sum)
                        
        return heapq.nlargest(3, rhombus)
