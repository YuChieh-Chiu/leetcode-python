class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """
        thought:
        - the prerequisites that two strings are close is as below
            (1) length of `word1` == length of `word2`
            (2) character in `word1` == character in `word2`
        - dig in the property of `operation 1` and `operation 2`, we can see that if the distribution of characters is the same, two strings would be `close`
            (1) `operation 1` can solve with character swapping between two characters with same number of occurrences
            (2) `operation 2` can solve with character transformation between two characters with different number of occurrences
        """
        if len(word1) != len(word2):
            return False
        if set(word1) != set(word2):
            return False
        word1_distribution = {}
        word2_distribution = {}
        for char in word1:
            if char in word1_distribution:
                word1_distribution[char] += 1
            else:
                word1_distribution[char] = 1
        for char in word2:
            if char in word2_distribution:
                word2_distribution[char] += 1
            else:
                word2_distribution[char] = 1
        if sorted(word1_distribution.values()) == sorted(word2_distribution.values()):
            return True
        else:
            return False
