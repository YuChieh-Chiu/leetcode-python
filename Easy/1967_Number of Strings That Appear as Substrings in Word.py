class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        """
        Thought:
        - Goal: Count how many strings in the `patterns` array are substrings of the given string `word`.
        - Idea: Iterate through each string in the `patterns` array and use Python's built-in `in` operator to check if it exists within `word`. Accumulate the total count of such matches.
        - Steps:
            1. Initialize a counter `total` to 0.
            2. Loop through each `pattern` in the `patterns` list.
            3. Check if `pattern` is a substring of `word` using the `in` keyword.
            4. If true, increment `total` by 1.
            5. Return the final `total` count.
        - Time Complexity: O(N * M * L), where N is the number of patterns, M is the length of `word`, and L is the average length of a pattern.
        - Space Complexity: O(1).
        """
        total = 0

        for pattern in patterns:
            if pattern in word:
                total += 1

        return total
