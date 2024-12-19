class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Thought:  
        - Problem Description:  
            - Given an m x n matrix, return all elements of the matrix in spiral order.  
        - Idea:  
            - The traversal follows a spiral pattern with four turning points in each cycle:  
                - [(m_start, n_end), (m_end, n_end), (m_end, n_start), (m_start + 1, n_start)]  
            - After completing each cycle:  
                - Increment `m_start` and `n_start` by 1.  
                - Decrement `m_end` and `n_end` by 1.  
            - In the final cycle, `m_start` equals `m_end`. 
        - Steps:  
            1. Initialize Variables:  
                - `m_start`, `m_end`, `n_start`, `n_end`: define the current boundary of the cycle.  
                - `spiral_output`: the output list to store elements in spiral order.  
            2. Traverse the Matrix in a While Loop:  
                - Continue the loop until `m_start` equals `m_end` or `n_start` equals `n_end`.  
            3. Handle the Last Cycle:  
                - Append the remaining elements within the current boundary to `spiral_output`.  
        """
        spiral_output = []

        m_start = n_start = m_current = n_current = 0
        m_end = len(matrix)-1
        n_end = len(matrix[0])-1
        while (m_start < m_end) and (n_start < n_end):
            spiral_output.append(matrix[m_current][n_current])
            if m_current == m_start:
                if n_current < n_end:
                    n_current += 1
                else:
                    m_current += 1
                continue
            if n_current == n_end:
                if m_current < m_end:
                    m_current += 1
                else:
                    n_current -= 1
                continue
            if m_current == m_end:
                if n_current > n_start:
                    n_current -= 1
                else:
                    m_current -= 1
                    if m_current == m_start:
                        break
                continue
            if n_current == n_start:
                if m_current > (m_start + 1):
                    m_current -= 1
                else:
                    n_current += 1
                    m_start += 1
                    n_start += 1
                    m_end -= 1
                    n_end -= 1
                continue

        if (m_start == m_end) and (n_start < n_end):        
            for i in range(n_start, n_end+1):
                spiral_output.append(matrix[m_current][i])
        elif (m_start < m_end) and (n_start == n_end):
            for i in range(m_start, m_end+1):
                spiral_output.append(matrix[i][n_current])
        elif (m_start == m_end) and (n_start == n_end):
            spiral_output.append(matrix[m_start][n_start])

        return spiral_output
