class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        """
        Thought:
        - Goal: Count the number of special letters in a string, where a letter is "special" if it appears in both uppercase and lowercase.
        - Idea: We can use set theory to find the intersection. The size of the set of all unique characters minus the size of the set of all unique case-insensitive characters will exactly equal the number of characters that appeared in both cases.
        - Steps:
            1. Create a set of the original `word` to get all unique characters (both upper and lower cases).
            2. Create a set of `word.lower()` to get all unique letters ignoring their case.
            3. Subtract the length of the second set from the first set. The difference represents the overlapping "special" letters.
            4. Return the calculated difference.
        - Time Complexity: O(N), where N is the length of the string `word`.
        - Space Complexity: O(N), where N is the length of the string `word`.
        """
        return len(set(word)) - len(set(word.lower()))
