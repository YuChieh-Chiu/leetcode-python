class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        """
        Thought:
        - Goal: Return the number of smooth descent periods.
        - Idea: 
            - Identify contiguous segments where prices decrease by exactly 1.
            - For a segment of descent length L (edges), the number of valid subarrays (excluding single elements) follows the arithmetic progression sum: (1 + L) * L / 2.
            - The final result is the sum of these combinations plus the total number of single-day periods (which is the length of the array).
        - Steps:
            1. Initialize `total` to 0 and `current_descent_len` to 0.
            2. Iterate through `prices` from the second element.
            3. If current price is exactly 1 less than previous, increment `current_descent_len`.
            4. If not, apply the formula to add valid periods from the previous segment to `total`, then reset `current_descent_len`.
            5. After the loop, apply the formula one last time for the final segment.
            6. Return `total` + length of `prices`.
        - Time Complexity: O(N)
            - We iterate through the `prices` array exactly once.
        - Space Complexity: O(1)
            - We only use a few integer variables for storage, no extra array is allocated.
        """
        total = 0
        current_descent_len = 0  # Represents the number of valid 'edges' in current run
        n = len(prices)

        for i in range(1, n):
            if prices[i-1] - prices[i] == 1:
                current_descent_len += 1
            else:
                # 結算上一段的組合數： (首項 + 末項) * 項數 / 2
                total += (1 + current_descent_len) * current_descent_len // 2
                current_descent_len = 0
        
        # 迴圈結束後，補算最後一段的組合數
        total += (1 + current_descent_len) * current_descent_len // 2

        return total + n
