class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        """
        Thought:
        - Goal: Find the kth (1-indexed) symbol in the nth row without constructing the entire row.
        - Rule/Constraint:
            - Start with '0' in row 1
            - Each '0' generates '01', each '1' generates '10' in the next row
            - 1 <= n <= 30, 1 <= k <= 2^(n-1)
        - Idea:
            - Instead of building the entire row, trace back from row n to row 1
            - Each position k in row n comes from position (k+1)//2 in row n-1 
            - Once we know the parent's value, determine child's value based on:
                - If parent = 0: left child (odd k) = 0, right child (even k) = 1
                - If parent = 1: left child (odd k) = 1, right child (even k) = 0
        - Steps:
            1. Build a trace path from row n back to row 1 using parent position formula: (k+1)//2
            2. Start from row 1 (value = 0) and propagate values forward to row n
            3. For each row, determine the value based on parent's value and position parity
        - Time Complexity: O(n)
        - Space Complexity: O(n)
        - Appendix: Recursive Approach
            - A more elegant solution uses recursion with O(n) time and O(n) call stack space
            - Base case: if n == 1, return 0
            - Recursive case: 
                - Find parent value: parent_val = kthGrammar(n-1, (k+1)//2)
                - Determine current value based on parent_val and whether k is odd/even
            - This eliminates the need for the row_loop list, making the code cleaner
        """
        if n == 1:
            return 0
        else:
            row_loop = [(k,0)]*n # [(loc, val)]

            while n > 1: # NOTE: n is 1-indexed
                n -= 1
                last_val = row_loop[n][0]
                row_loop[n-1] = ((last_val + 1)//2, 0)

            for idx, (loc, val) in enumerate(row_loop[1:], 1):
                if row_loop[idx-1][1] == 0:
                    if loc % 2 == 0:
                        new_val = 1
                    else:
                        new_val = 0
                else:
                    if loc % 2 == 0:
                        new_val = 0
                    else:
                        new_val = 1
                row_loop[idx] = (loc, new_val)

            return row_loop[-1][1]
