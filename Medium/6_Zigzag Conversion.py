class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        thought:
        - we want to convert `s` to a ZIGZAG format and then read it line by line
        - the feature of the ZIGZAG format is as below:
            (1) the column 0 should be filled
            (2) the character in column 1 should locate on (numRows-2)
            (3) the character in column 2 should locate on (numRows-3)
            (4) ...
            (5) the character in column numRows-1 should be filled again
            (6) ...
        - the process we should follow is as below:
            (1) if numRows == 1, just return `s`
            (2) else, draw ZIGZAG graph
            (3) and then read line by line (line=row)
        """
        if numRows == 1:
            return s
        output_s = ""
        zigzag = [""]*numRows
        row = col = 0
        for c in s:
            if (col == 0) | (col % (numRows-1) == 0):
                zigzag[row] += c
                row += 1
                if row == numRows:
                    col += 1
                    row = 0
            else:
                zigzag[(col % (numRows-1))*(-1)-1] += c # locate on (col % (numRows-1))*(-1)-1
                col += 1 
        output_s = "".join(zigzag)
        return output_s
