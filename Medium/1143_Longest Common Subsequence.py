class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Thought:
        - Goal:
            - Given two strings `text1` and `text2`, find the length of their longest common subsequence.
        - Definition of Common Subsequence:
            - A common subsequence is a subsequence that appears in both strings in the same relative order.
            - Example: For "abc" and "aec", the longest common subsequence is "ac" with length 2.
        - Idea:
            - We can solve this problem by comparing characters at each position of both strings.
            - At each step, we have different choices based on whether characters match or not.
            - Since same positions can be reached through different paths (subproblems overlap), we should use dynamic programming with memoization.
        - Steps:
            1. Initialization:
                - Create a dictionary `memo = {}` to store the results for each (i, j) position pair.
            2. Recursive Function:
                - Base Case:
                    - If i == len(text1) or j == len(text2), we've reached the end of one string, so return 0 (no more characters to match).
                - Recursive Relation:
                    - If text1[i] == text2[j]: characters match
                        - Current match contributes 1 + result from next positions: 1 + dp(i+1, j+1)
                    - If text1[i] != text2[j]: characters don't match
                        - Try two options and take the maximum:
                            - Skip character in text1: dp(i+1, j)
                            - Skip character in text2: dp(i, j+1)
                        - Return max(dp(i+1, j), dp(i, j+1))
            3. Output:
                - Start the recursion from position (0, 0) to find the longest common subsequence from the beginning of both strings.
        - Topics:
            - Dynamic Programming, Memoization
        """
        
        # Step 1: Initialize memoization dictionary
        memo = {}
        
        # Step 2: Define recursive function with memoization
        def dp(i: int, j: int) -> int:
            # Check if result is already computed
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Base case: reached end of either string
            if i == len(text1) or j == len(text2):
                return 0
            
            # Recursive relation
            if text1[i] == text2[j]:
                # Characters match: include current match + solve remaining
                result = 1 + dp(i + 1, j + 1)
            else:
                # Characters don't match: try both options and take maximum
                result = max(
                    dp(i + 1, j),    # Skip character in text1
                    dp(i, j + 1)     # Skip character in text2
                )
            
            # Store result in memo and return
            memo[(i, j)] = result
            return result
        
        # Step 3: Start recursion from beginning of both strings
        return dp(0, 0)
