class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        """
        Thought:
        - Goal: Count the number of good substrings of length 3 in the string `s` (a good substring contains no duplicate characters).
        - Idea: Use a sliding window of fixed size 3 to iterate through the string. For each window, use a hash set to check if all characters are unique.
        - Steps:
            1. Initialize a `count` variable to 0.
            2. Iterate through the string with an index `i` from 0 up to `len(s) - 3`.
            3. Extract the substring of length 3 starting at index `i`.
            4. Convert the substring into a set. If the length of the set is exactly 3, it means all characters are unique; increment the `count`.
            5. Return the final `count`.
        - Time Complexity: O(N), where N is the length of the string `s`.
        - Space Complexity: O(1).
        """
        count = 0

        for i in range(len(s)-2):
            sliced = s[i:i+3]
            if len(set(sliced)) == 3:
                count += 1
        
        return count
