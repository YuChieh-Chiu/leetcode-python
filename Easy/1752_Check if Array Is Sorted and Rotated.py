class Solution:
    def check(self, nums: List[int]) -> bool:
        """
        Thought:
        -  Goal: Determine if a given array was originally sorted in non-decreasing order, then rotated some number of positions (including zero).
        -  Constraints:
            - 1 <= nums.length <= 100
            - 1 <= nums[i] <= 100
        - Idea: 
            - A rotated sorted array can only have at most one "break point" where nums[i] > nums[i+1]
            - Find the break point where current element is smaller than the previous element
            - Split the array into two slices: before the break point and from the break point onwards
            - For a valid rotated array:
                - The first slice must be non-decreasing (already validated during traversal)
                - The second slice must be non-decreasing
                - Every element in the second slice must be smaller than the first element of the first slice
                - If no break point is found, the array is already sorted in non-decreasing order
        - Steps:
            1. **Find the rotation break point**: Traverse the array to find the first position where nums[i] < nums[i-1]
            2. **Handle no break point case**: If no break point found, return true (array is already sorted)
            3. **Validate second slice**: Check if elements from break point onwards are in non-decreasing order
            4. **Check rotation constraint**: Ensure every element in the second slice is smaller than the first element of the first slice
            5. **Return result**: Return true if all conditions are met, false otherwise
        - Time Complexity: O(n)
        - Space Complexity: O(1)
        """
        # 尋找旋轉斷點
        split_index = None
        prev_num = 0
        
        for i, num in enumerate(nums):
            if num < prev_num:
                split_index = i
                break
            prev_num = num
        
        # 如果沒有斷點，表示陣列已經是非降冪排列，直接回傳 true
        if split_index is None:
            return True
        
        # 檢查第二個 slice 是否為非降冪，且每個值都小於第一個 slice 的起始值
        prev_num = 0
        first_slice_start = nums[0]
        
        for num in nums[split_index:]:
            if num < prev_num or num > first_slice_start:
                return False
            prev_num = num
        
        return True
