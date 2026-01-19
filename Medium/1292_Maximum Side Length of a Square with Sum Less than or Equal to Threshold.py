class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        """
        Thought:
        - Goal: Find the maximum side-length of a square whose sum is less than or equal to a given threshold.
        - Idea: 
            1. 2D Prefix Sum Construction: Create a matrix `ps` where `ps[i][j]` represents the sum from `mat[0][0]` to `mat[i-1][j-1]`.
               >>> Formula: ps[i][j] = mat[i-1][j-1] + ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1].
            2. Range Sum Query: Calculate the sum of any square with side length `k` and  bottom-right corner (r, c) in O(1) time.
               >>> Formula: sum = ps[r][c] - ps[r-k][c] - ps[r][c-k] + ps[r-k][c-k].
            3. Greedy Sliding Window: Iterate through each cell and check only if a square with side (max_len + 1) exists. Since we only need the global maximum, we don't need to re-check smaller lengths.
        - Steps:
            1. Build a (M+1) x (N+1) prefix sum matrix to handle boundary conditions easily.
            2. For each cell (r, c), check if the threshold is satisfied for side length (max_len + 1).
            3. Update max_len if valid and skip the rest of the current row to optimize.
        - Time Complexity: O(M * N) - Each cell is visited once, and each sum is O(1).
        - Space Complexity: O(M * N) - Required for the prefix sum matrix.
        """
        R, C = len(mat), len(mat[0])
        ps = [[0] * (C + 1) for _ in range(R + 1)]
        
        # 關鍵點 1: 建構二維前綴和
        for r in range(R):
            for c in range(C):
                ps[r + 1][c + 1] = mat[r][c] + ps[r][c + 1] + ps[r + 1][c] - ps[r][c]
        
        max_len = 0
        for r in range(1, R + 1):
            for c in range(1, C + 1):
                cur_target_len = max_len + 1
                
                if r >= cur_target_len and c >= cur_target_len:
                    # 關鍵點 2: 應用公式計算任意正方形的和
                    total = (ps[r][c] 
                             - ps[r - cur_target_len][c] 
                             - ps[r][c - cur_target_len] 
                             + ps[r - cur_target_len][c - cur_target_len])
                    
                    if total <= threshold:
                        max_len += 1
                        break
                        
        return max_len
