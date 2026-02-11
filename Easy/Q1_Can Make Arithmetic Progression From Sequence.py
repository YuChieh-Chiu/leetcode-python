class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        """
        Thought:
        - Goal: Determine if an array can be rearranged to form an arithmetic progression where the difference between consecutive elements is constant.
        - Idea: An arithmetic progression is easiest to verify when elements are in order. By sorting the array, we only need to check if the gap between every two adjacent numbers remains the same.
        - Steps:
            1. Sort the input array in ascending order.
            2. Calculate the common difference between the first two elements.
            3. Iterate through the rest of the array, comparing each adjacent pair's difference to the common difference.
            4. Return false if any difference deviates; otherwise, return true.
        - Time Complexity: O(n log n)
        - Space Complexity: O(1)
        """
        # 1. 排序
        arr.sort()
        
        # 2. 定義基準差值
        diff = arr[1] - arr[0]
        
        # 3. 遍歷並提早回傳
        for i in range(2, len(arr)):
            if arr[i] - arr[i-1] != diff:
                return False
        
        return True
