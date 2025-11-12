import math
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
        Thought:
        - Goal: Minimize operations to make all elements of `nums` equal to 1 by replacing nums[i] or nums[i+1] with gcd(nums[i], nums[i+1]).
        - Idea: The overall minimum operations is the sum of (Ops to generate the first '1') + (Ops to propagate '1' to the rest of the array).
        - Steps:
            1. Check for the trivial case: If the array already contains '1's (m of them), the first phase is 0 operations. The total is N - m.
            2. Check for impossibility: If the GCD of the entire array is greater than 1, return -1.
            3. Find Min Length (L_min): Use nested loops (start/end) to find the shortest contiguous subarray whose GCD is 1. This requires (L_min - 1) operations in the first phase. Use a rolling GCD calculation for efficiency.
            4. Calculate Result: Total Ops = (L_min - 1) [Phase 1] + (N - 1) [Phase 2].
        - Time Complexity: O(N^2 * log(max(nums)))
        - Space Complexity: O(1)
        """
        length = len(nums)
        
        # 1. 處理特殊情況：如果陣列中已經有 1
        count_ones = nums.count(1)
        if count_ones > 0:
            # 只需要 N - m 次操作來將其餘 N-m 個非 1 元素變成 1
            return length - count_ones

        # 2. 檢查不可行條件：如果整個陣列的 GCD > 1
        # 循環計算整體 GCD
        current_gcd_overall = nums[0]
        for num in nums[1:]:
            current_gcd_overall = math.gcd(current_gcd_overall, num)
            
        if current_gcd_overall > 1:
            return -1

        # 3. 計算並找出 GCD=1 的最短子列表長度 L_min
        L_min = float('inf') # 使用 'inf' 更標準
        
        # 外層迴圈：起點
        for start in range(length):
            # 內層迴圈開始前，初始化 current_gcd 為子列表的第一個元素
            current_gcd = nums[start]
            
            # 內層迴圈：終點
            for end in range(start + 1, length):
                # 滾動 GCD 計算： current_gcd = gcd(previous_gcd, nums[end])
                current_gcd = math.gcd(current_gcd, nums[end])
                
                if current_gcd == 1:
                    sub_length = end - start + 1
                    L_min = min(L_min, sub_length)
                    
                    # 找到以 start 為起點的最短 L 後，可以跳出內層迴圈
                    break
        
        # 4. 計算出最終的最少操作次數 (L_min - 1) + (N - 1)
        # 由於 L_min 必然 <= N (因為整體 GCD=1)，這裡不需要再檢查 L_min == inf
        return (L_min - 1) + (length - 1)
