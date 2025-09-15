class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        """
        Thought:
        - Goal: Count how many complete words can be typed from the given text, where a word is considered "typeable" if it contains no broken letters.
        - Idea: Split the text into individual words, convert broken letters to a set for O(1) lookup, then check each word character by character. If any character in a word matches a broken letter, that word cannot be typed.
        - Steps:
            1. Initialize a counter `can_be_typed` to track typeable words
            2. Split the input text into a list of words using space as delimiter
            3. Convert `brokenLetters` string to a set for efficient lookup
            4. For each word in the text:
                - Increment the counter (assume the word can be typed)
                - Check each character in the word against the broken letters set
                - If any character is found in broken letters, decrement the counter and break to next word
            5. Return the final count of typeable words
        - Time Complexity: O(n) where n is the total number of characters in the text
        - Space Complexity: O(n + b) where n is the total number of characters in the text and b is the number of broken characters
        """
        can_be_typed = 0

        text = text.split(" ")
        brokenLetters = set(brokenLetters)

        for word in text:
            can_be_typed += 1
            for char in word:
                if char in brokenLetters:
                    can_be_typed -= 1
                    break

        return can_be_typed
