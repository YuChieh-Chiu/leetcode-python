class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        """
        Thought:
        - Goal: Find the minimum number of adjacent row swaps to make all cells above the main diagonal zeros.
        - Idea: Each row i must have at least (n - 1 - i) trailing zeros. We use a greedy approach to find the nearest satisfying row and move it to the current position.
        - Steps:
            1. Pre-calculate the number of trailing zeros for each row.
            2. Iterate through each row position i from 0 to n-1.
            3. Calculate the 'required' number of trailing zeros: (n - 1 - i).
            4. Search from index i downwards to find the first row j meeting the requirement.
            5. If found, add (j - i) to swaps, then pop index j and insert at index i.
            6. Return -1 if no such row is found for any position i.
        - Time Complexity: O(n^2)
            Note: While it looks like O(n^3) due to nested loops and pop/insert operations, it is  actually O(n^2) because the 'break' statement ensures that the O(n) list manipulation (pop and insert) is executed at most once per outer loop iteration. 
            Total complexity: O(n^2) for preprocessing + O(n * (n + n)) for the greedy search and shift.
        - Space Complexity: O(n)
            Storing the trailing zeros for each row requires O(n) extra space.
        """
        n = len(grid)
        # 1. 預處理：計算每一列末尾連續 0 的數量
        trailing_zeros = []
        for row in grid:
            count = 0
            for val in reversed(row):
                if val != 0: break
                count += 1
            trailing_zeros.append(count)
        
        total_swaps = 0
        # 2. 貪婪排序
        for i in range(n):
            # 每一列 i 至少需要的末尾 0 數量
            required = n - 1 - i
            # 從當前位置 i 往下尋找第一個符合條件的列
            for j in range(i, n):
                if trailing_zeros[j] >= required:
                    # 找到目標，累加交換步數
                    total_swaps += (j - i)
                    # 模擬交換：將該列移到當前位置，其餘順延
                    row_to_move = trailing_zeros.pop(j)
                    trailing_zeros.insert(i, row_to_move)
                    break
            else:
                # 如果整層迴圈都沒 break，代表找不到符合條件的列
                return -1
                
        return total_swaps
