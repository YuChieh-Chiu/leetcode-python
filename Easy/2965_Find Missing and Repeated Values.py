class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        """
        Thought:
        - Goal:  
            - Find the missing value and the repeated value in the matrix `grid`.  
        - Constraints:  
            - 1 <= grid[i][j] <= n*n 
            - Exactly one number appears twice, and exactly one number is missing.  
        - Idea:  
            - We can use a dictionary to track the occurrence count of each value. The number with an occurrence count of 0 is the missing value, and the number with an occurrence count of 2 is the repeated value.  
        - Steps:  
            1. Initialize a dictionary with keys ranging from 1 to n*n, all set to 0.  
            2. Traverse the matrix `grid` and update the dictionary's count for each encountered value.  
            3. Identify the key whose value is 2 (repeated value) and the key whose value is 0 (missing value).  
        """

        value_cnts = {str(i): 0 for i in range(1, len(grid)*len(grid[0])+1)}

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                key = str(grid[i][j])
                value_cnts[key] += 1

        not_unique = [(key, val) for key, val in value_cnts.items() if val != 1]
        not_unique = sorted(not_unique, key=lambda x: x[1], reverse=False)
        repeated_and_missing = [int(not_unique[1][0]), int(not_unique[0][0])]
        
        return repeated_and_missing
