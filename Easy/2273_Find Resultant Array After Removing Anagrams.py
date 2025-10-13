class Solution:
    def checkAnagrams(self, left: str, right: str) -> bool:
        """
        Check if two strings are anagrams of each other.
        
        Args:
            left: First string to compare
            right: Second string to compare
            
        Returns:
            True if the strings are anagrams, False otherwise
        """
        # Early exit: if character sets differ, they cannot be anagrams
        if set(left) != set(right):
            return False

        # Verify each character appears with the same frequency
        for char in set(left):
            if left.count(char) != right.count(char):
                return False
            
        return True

    def removeAnagrams(self, words: List[str]) -> List[str]:
        """
        Thought:
        - Goal: Return the array after removing all consecutive anagrams
        - Operation Definition: Delete words[i] if words[i-1] and words[i] are anagrams
        - Idea: Use two pointers to track consecutive non-anagram words. When we find a word that is not an anagram of the previous word, we keep the previous word and move our reference pointer forward.
        - Steps:
            1. Initialize left pointer at index 0
            2. Append a sentinel value (empty string) to handle the last group
            3. Iterate with right pointer from index 1 to end
            4. If words[left] is not an anagram of words[right]:
               - Add words[left] to result
               - Move left pointer to right pointer position
            5. Return the result array
        - Time Complexity: O(n * m) where n is the number of words and m is the maximum length of a word. We iterate through n words and check anagrams which takes O(m) per comparison.
        - Space Complexity: O(n) for storing the result array
        """
        left = 0
        # Append sentinel to ensure the last non-anagram group is included
        words.append("")
        words_without_anagram = []
        
        for right in range(1, len(words)):
            # When we find a non-anagram, save the word at left pointer
            if not self.checkAnagrams(words[left], words[right]):
                words_without_anagram.append(words[left])
                left = right
                
        return words_without_anagram
