class Solution:
    def minLength(self, s: str) -> int:
        """
        thought:
    - our goal is to remove any occurrence of the substrings 'AB' or 'CD' from 's' and return the length of the final string.
        - note that after removing a substring, the remaining string may concatenate, potentially forming new 'AB' or 'CD' substrings.
    - we will traverse the string 's' character by character, repeatedly checking for the substrings 'AB' or 'CD' until none remain.
    - to efficiently build the new string while traversing 's', we can use a `Last In, First Out (LIFO)` data structure to simulate the removal process.
    - the process follows these steps:
        (1) use a loop to repeatedly traverse the string 's' until no 'AB' or 'CD' substrings are found.
        (2) for each character, add it to the new string (the LIFO structure).
            - if the last characters and the added character in the new string form 'AB' or 'CD', remove both from the new string.
        (3) once the loop finishes and no more substrings are found, return the length of the new string.
        """
        new_string = ""
        while True:
            occurrence = 0
            for char in s:
                if new_string == "":
                    new_string += char
                else:
                    if new_string[-1] + char in ["AB", "CD"]: # LIFO
                        new_string = new_string[:-1] 
                        occurrence += 1
                    else:
                        new_string += char
            s = new_string
            new_string = ""
            if occurrence == 0:
                break
        return len(s)
