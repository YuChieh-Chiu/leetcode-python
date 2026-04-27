class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        """
        Thought:
        - Goal: Determine if there is a valid path connecting the top-left cell (0, 0) to the bottom-right cell (m-1, n-1) in the grid following the street rules.
        - Idea: Treat the grid as a graph and use Depth-First Search (DFS) to explore paths. We maintain a state machine (`rule` dictionary) that maps each street type to its allowed directions and the valid street types it can connect to.
        - Steps:
          1. Define a `rule` dictionary specifying connectivity for all 6 street types.
          2. Start a DFS traversal from (0,0), assuming an initial valid set of all possible streets.
          3. Base Cases: Return False if the cell is already visited or if the current street type does not match the allowed `valid_set` from the previous cell.
          4. If it's a valid cell, check if we have reached the destination `(m-1, n-1)`. If so, return True.
          5. Mark the current cell as visited to prevent cycles.
          6. Iterate through the allowed directions for the current street type, calculate the next coordinates, perform boundary checks, and recursively call DFS. Return True immediately if any path succeeds.
        - Time Complexity: O(m * n), where m and n are the dimensions of the grid.
        - Space Complexity: O(m * n).
        """
        m, n = len(grid), len(grid[0])
        
        rule = {
            1: {(0, 1): {1, 3, 5}, (0, -1): {1, 4, 6}},
            2: {(1, 0): {2, 5, 6}, (-1, 0): {2, 3, 4}},
            3: {(1, 0): {2, 5, 6}, (0, -1): {1, 4, 6}},
            4: {(1, 0): {2, 5, 6}, (0, 1): {1, 3, 5}},
            5: {(-1, 0): {2, 3, 4}, (0, -1): {1, 4, 6}},
            6: {(0, 1): {1, 3, 5}, (-1, 0): {2, 3, 4}}
        }

        visited = set()

        def dfs(row, col, valid_set):
            if (row, col) in visited:
                return False

            current = grid[row][col]

            if current not in valid_set:
                return False
                
            if row == m - 1 and col == n - 1:
                return True

            visited.add((row, col))

            for (dr, dc), next_valid_set in rule[current].items():
                next_row, next_col = row + dr, col + dc
                if next_row < 0 or next_row >= m or next_col < 0 or next_col >= n:
                    continue                
                if dfs(next_row, next_col, next_valid_set):
                    return True

            return False

        return dfs(0, 0, {1, 2, 3, 4, 5, 6})
