class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        """
        Thought:
        - Goal: Calculate the total score of a balanced parentheses string according to the given nested scoring rules.
        - Idea: Only the innermost pairs "()" contribute directly to the score. Every outer wrapping layer doubles that pair's score. Therefore, each "()" at 0-indexed depth `d` contributes `2^d` to the final sum.
        - Steps:
            1. Track the current nesting depth (`depth`) and the previous character (`prev_char`).
            2. Iterate through each character in the string:
               - If '(', increase `depth` by 1.
               - If ')':
                   - If preceded immediately by '(', add `1 << (depth - 1)` to the total score.
                   - Decrease `depth` by 1.
               - Update `prev_char`.
            3. Return the accumulated score.
        - Time Complexity: O(N), where N is the length of the string s.
        - Space Complexity: O(1), using only constant extra space.
        """
        score = 0
        depth = 0
        prev_char = ''

        for char in s:
            if char == '(':
                depth += 1
            else:
                if prev_char == '(':
                    score += 1 << (depth - 1)
                depth -= 1
            prev_char = char

        return score
