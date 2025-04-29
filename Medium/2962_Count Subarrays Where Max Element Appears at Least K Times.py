class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        """
        Thought:
        - Goal: 
            - Find the number of subarrays in which the maximum value in `nums` appears at least `k` times.
        - Idea:
            - Since we are looking for subarrays where the maximum number appears **at least** `k` times, it is difficult to define the sliding window directly for such a condition.
            - Instead, we reverse the logic:
                - Total number of subarrays = n * (n + 1) / 2
                - From this, subtract the number of subarrays where the maximum value appears **at most** `k - 1` times.
                - This reformulation makes it easier to implement a sliding window, where we simply ensure the window contains no more than `k - 1` occurrences of the maximum value.
        - Steps:
            1. Find the maximum value in the array.
            2. Implement a helper function using the sliding window technique to count subarrays that contain at most `k - 1` instances of the maximum value.
                - Initialize result to 0, left pointer to 0, and a counter to track maxNum occurrences.
                - For each right pointer:
                    1. If `nums[right]` equals maxNum, increment the counter.
                    2. If the count exceeds `k - 1`, move the left pointer rightward and decrement the count when a maxNum is removed.
                    3. At each step, the number of valid subarrays ending at `right` is `(right - left + 1)`.
            3. Subtract the result of step 2 from the total number of subarrays to get the final answer.
        """
        maxNum = max(nums)
        less_than_k = self.countSubarraysWithAtMost(nums, maxNum, k - 1)
        return len(nums) * (len(nums) + 1) // 2 - less_than_k

    def countSubarraysWithAtMost(self, nums, maxNum, limit):
        """
        Count the number of subarrays that contain at most `limit` occurrences of `maxNum`.
        """
        result = 0
        left = 0
        count = 0  # Number of maxNum in the current window
        
        for right in range(len(nums)):
            if nums[right] == maxNum:
                count += 1
            
            while count > limit:
                if nums[left] == maxNum:
                    count -= 1
                left += 1
            
            result += right - left + 1
        
        return result
