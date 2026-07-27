class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Thought:
        - Goal: Find two distinct elements nums[i] and nums[j] to maximize (nums[i] - 1) * (nums[j] - 1).
        - Idea: The maximum product is obtained by selecting the two largest numbers in the array.
        - Steps:
            1. Traverse the array to track the largest (max1) and second-largest (max2) numbers.
            2. Calculate and return (max1 - 1) * (max2 - 1).
        - Time Complexity: O(n), where n is the length of nums, as we iterate through the array once.
        - Space Complexity: O(1), since we only use two variables (max1 and max2) for storage.
        """
        max1 = max2 = 0

        for num in nums:
            if num > max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num

        return (max1 - 1) * (max2 - 1)
