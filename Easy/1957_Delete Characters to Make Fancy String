class Solution:
    def makeFancyString(self, s: str) -> str:
        """
        Thought:
        - Goal: Return the final fancy string.
        - Definition: A fancy string is a string in which no three consecutive characters are the same.
        - Idea:  
            - Track two variables during traversal:
                1. `consecutive_char`: Tracks the current repeating character. It's updated whenever a different character is encountered.
                2. `duplication_count`: Counts how many times `consecutive_char` appears consecutively.  
                    - If it reaches 3, skip appending the current character.  
                    - If a new character is encountered, reset the count to 1.
        - Steps:
            1. Initialize three variables:
                - `fancy_str`: An empty string to store the final result.
                - `consecutive_char`: Initialized as the first character of the string.
                - `duplication_count`: Initialized to 0.
            2. Traverse through the string `s`:
                - If the current character equals `consecutive_char`:  
                    - Increment `duplication_count` by 1.  
                    - If `duplication_count` is less than or equal to 2, append the character to `fancy_str`. Otherwise, skip it.
                - Else (character is different):  
                    - Update `consecutive_char` to the current character.  
                    - Reset `duplication_count` to 1.  
                    - Append the current character to `fancy_str`.
            3. Return `fancy_str`.
        """
        fancy_str = ""
        consecutive_char = s[0]
        duplication_count = 0

        for char in s:
            if char == consecutive_char:
                if (duplication_count + 1) != 3:
                    fancy_str += char
                    duplication_count += 1
            else:
                fancy_str += char
                consecutive_char = char
                duplication_count = 1
        
        return fancy_str
