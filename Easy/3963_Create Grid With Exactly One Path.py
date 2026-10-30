class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        """
        Thought:
        - Goal: Construct an m x n grid consisting of '.' and '#' such that there exists exactly one valid path from (0, 0) to (m - 1, n - 1) moving only right or down.
        - Idea: Build a deterministic 'L-shaped' path. Traverse horizontally across the first row to the top-right corner, then descend vertically along the last column to the destination. Fill all remaining cells with '#' to prevent branching.
        - Steps:
            1. Generate the first row containing n consecutive free cells ('.').
            2. For the subsequent m - 1 rows, generate a string with n - 1 obstacle cells ('#') followed by 1 free cell ('.').
            3. Combine and return the rows as the completed grid.
        - Time Complexity: O(m * n) to construct strings spanning the entire m x n cells.
        - Space Complexity: O(m * n) auxiliary space required to store the resulting grid.
        """
        grid = []

        for row in range(m):
            if row == 0:
                grid.append('.'*n)
            else:
                grid.append('#'*(n-1)+'.')

        return grid
