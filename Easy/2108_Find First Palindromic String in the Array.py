class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        """
        Thought:
        - Goal: Find the first palindromic string in the array. If there is no such string, return an empty string "".
        - Idea: Cut the string in half. Pop out the last character from the left side of the string if the first character in the right side of the string is the same as it.
        - Steps:
            1. Initialize a boolean variable `is_palindromic` to record whether the current string is palindromic or not.
            2. Traverse through the list `words`.
                For each string:
                2-1. Find the left part and the right part of the string
                    - if the length of the string is odd, the range of the left part would be the slice from the 0-index to the floor value of the index of the middle point; the range of the right part would be the slice from the ceiling value of the index of the middle point to the last index.
                    - if the length of the string is even, the range of the left part would be the slice from the 0-index to the value of the index of the middle point; the range of the right part would be the slice from the next value of the index of the middle point to the last index.
                2-2. Traverse through the right part and compare the current value with the value popped out from the end of the left part
                    - if the two characters are the same, continue.
                    - if the two characters are different, break the loop.
            3. If we have already found the palindromic string, return the value. If there's no palindromic string, return an empty string.
        - Time Complexity: O(n * m) where n is the number of words and m is the average length of words
        - Space Complexity: O(m) where m is the length of the longest word
        """
        is_palindromic = False

        for word in words:
            is_palindromic = True
            length = len(word)
            
            if length % 2 != 0:
                left_part = word[:length//2]
                right_part = word[length//2+1:]
            else:
                left_part = word[:length//2]
                right_part = word[length//2:]
            
            for val in right_part:
                if val != left_part[-1]:
                    is_palindromic = False
                    break
                else:
                    left_part = left_part[:-1]
            
            if is_palindromic:
                return word

        return ""
