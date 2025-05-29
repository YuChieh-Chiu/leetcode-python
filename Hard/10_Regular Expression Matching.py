from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Thought:
        - Goal: Implements a simplified version of re.fullmatch(p, s) without using the re module.
        - Constraints:
            - p consists of lowercase letters, '.', and '*' 
            - s consists of lowercase letters only
        - Idea:
            - '.' and lowercase letters represent a one-to-one match.
            - '*' is the only operator that allows flexible matching, so it requires special handling.
            - The goal is to perform a **full match**, meaning the entire string s must match the entire pattern p exactly.
        - Approach:
            - Use recursion with memoization (top-down dynamic programming).
            - At each step, determine whether the current positions in p and s match, then recursively check the remainder.
            - The recursion ends successfully only when both p and s are fully consumed.
        - Steps:
            1. Define a recursive function `recursive(i, j)` which checks whether p[i:] matches s[j:].
            2. Base case: If p is fully consumed, return True only if s is also fully consumed.
            3. Recursive logic:
                - Check if the current characters match (either identical or '.' in pattern).
                - If the next character in p is '*':
                    - Try two branches:
                        1. Skip "current character + *" in the pattern (zero occurrences).
                        2. If the current character matches, consume one character from s and try again.
                - If the next character in p is not '*':
                    - Proceed to the next positions in both p and s only if the current characters match.
        """
        @lru_cache(None)
        def recursive(i: int, j: int) -> bool:
            # Base case: if pattern is exhausted, s must also be exhausted
            if i == len(p):
                return j == len(s)

            # Check if the current characters match
            first_match = j < len(s) and (p[i] == s[j] or p[i] == '.')

            # If the next character in p is '*', consider both matching 0 times and consuming one character
            if i + 1 < len(p) and p[i + 1] == '*':
                return recursive(i + 2, j) or (first_match and recursive(i, j + 1))
            else:
                # Regular case: move to the next characters if the current ones match
                return first_match and recursive(i + 1, j + 1)

        return recursive(0, 0)

# import re
# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         is_match = re.fullmatch(p, s)
#         return True if is_match else False
