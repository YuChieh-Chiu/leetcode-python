class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        """
        Thought:
        - Goal:
            - Return the corresponding column number of the given column title.  
        - Examples:
            - If `columnTitle = "A"`, the output is `1`.  
            - If `columnTitle = "AB"`, the output is calculated as `1*(26**(2-0-1)) + 2 = 28`.  
            - If `columnTitle = "ZY"`, the output is calculated as `26*(26**(2-0-1)) + 25 = 701`.  
        - Steps: 
            1. Initialize a variable `colNumber` with the numeric value of the last character in `columnTitle`.  
            2. If `columnTitle` consists of only one character, return `colNumber`.  
            3. Iterate through all characters in `columnTitle` except the last one:  
                - Compute the numeric value of the character and update `colNumber` using the formula:  
                (ord(char) - 64) * (26 ** (len(columnTitle) - index - 1)
            4. Return `colNumber`.  
        """
        colNumber = ord(columnTitle[-1]) - 64
        length = len(columnTitle)
        
        if length == 1:
            return colNumber

        for i in range(length-1):
            colNumber += (ord(columnTitle[i])-64) * (26 ** (length-i-1))

        return colNumber
