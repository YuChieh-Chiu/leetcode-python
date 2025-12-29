class Solution:
    def __init__(self):
        self.memo = {}

    def verticalSearch(self, next_row: str, allowed_dict: dict):
        """
        Check if the current row can eventually build up to the pyramid top.
        Uses memoization to skip redundant row strings.
        """
        if next_row in self.memo:
            return self.memo[next_row]

        if len(next_row) == 1: # Reach the top of the pyramid
            return True

        # Delegate the task of generating the next row to horizontalSearch
        result = self.horizontalSearch(next_row, 0, "", allowed_dict)

        self.memo[next_row] = result
        return result

    def horizontalSearch(self, current: str, i: int, next_row: str, allowed_dict: dict):
        """
        Backtracking to generate all possible strings for the next level.
        Once a full next_row is formed, it triggers verticalSearch.
        """
        if i == len(current) - 1:
            return self.verticalSearch(next_row, allowed_dict)
        
        # Get all possible top blocks for the current pair of bottom blocks
        upper = allowed_dict.get(current[i: i+2], None)

        if not upper: # No valid triangular pattern found for this pair
            return False

        # Try every possible character for the current position in the next row
        for char in upper:
            passed = self.horizontalSearch(current, i + 1, next_row + char, allowed_dict)
            if passed:
                return True

        return False

    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        """
        Thought:
        - Goal: Determine if a pyramid can be built up to a single block using a given base and allowed triangular patterns.
        - Idea: 
            Utilize a layered Depth-First Search (DFS) approach. The problem is decomposed into two parts: 
            1. Vertical Search (row by row progression) 
            2. Horizontal Search (generating all possible valid strings for the next level).
        - Steps:
            1. Preprocess the 'allowed' patterns into a hash map (dictionary) for O(1) lookups.
            2. Start 'verticalSearch' from the bottom row.
            3. Within each row, use 'horizontalSearch' (backtracking) to form the next row based on valid pairs.
            4. Memoize each row string to avoid redundant computations of the same sub-pyramid.
            5. Return True if any valid path reaches a string of length 1.
        - **Time Complexity**: O(N * K^N), where N is the length of bottom and K is the average number of allowed options per pair.
        - **Space Complexity**: O(N^2 + S), where N is the depth of the recursion stack and S is the number of states in memo.
        """
        # Preprocess allowed list into a dictionary for efficient lookup
        allowed_dict = {}
        for char in allowed:
            lower = char[:2]
            upper = char[2]
            if lower in allowed_dict:
                allowed_dict[lower].append(upper)
            else:
                allowed_dict[lower] = [upper]
            
        return self.verticalSearch(bottom, allowed_dict)
