class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        """
        Thought:
        - Goal: Determine if s1 and s2 can be made equal by swapping characters at indices with an even distance (i.e., j - i is even).
        - Idea: An even-distance swap means characters at even indices can only move to other even indices, and odd to odd. Therefore, s1 and s2 can become equal if and only if the multiset of characters at even positions are identical, and similarly for odd positions.
        - Steps:
            1. Extract all characters at even indices (0, 2, 4...) for both s1 and s2.
            2. Extract all characters at odd indices (1, 3, 5...) for both s1 and s2.
            3. Compare the character frequency counts for the even-indexed groups.
            4. Compare the character frequency counts for the odd-indexed groups.
            5. Return true if both even and odd groups match, otherwise return false.
        - Time Complexity: O(n), where n is the length of the strings.
        - Space Complexity: O(n) to store the characters/counts of the split groups (or O(1) if considering fixed alphabet size).
        """
        odd_match = Counter(s1[1::2]) == Counter(s2[1::2])
        even_match = Counter(s1[::2]) == Counter(s2[::2])

        return odd_match and even_match
