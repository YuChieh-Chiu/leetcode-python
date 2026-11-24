class Solution:
    def maxLength(self, nums: List[int]) -> int:
        """
        Thought:
        - Goal: Find the length of the longest contiguous subarray where prod(arr) == lcm(arr) * gcd(arr).
        - Idea: Use a sliding window with two pointers (left and right). Since any subarray of length 2 is always product equivalent, the minimum possible answer is 2. We expand the window to the right whenever the current subarray is valid, and shrink it from the left when it becomes invalid.
        - Steps:
            1. Initialize left = 0, right = 2 (exclusive), and longest = 2
            2. While right <= len(nums), slice the current window nums[left:right]
            3. Check if math.prod(subarray) == math.lcm(*subarray) * math.gcd(*subarray)
            4. If valid, update longest with max(longest, right - left) and increment right to expand the window
            5. Otherwise, increment left to shrink the window
            6. Return longest after the loop finishes
        - Time Complexity: O(N^2), where N is the length of nums. The two pointers move at most 2N times, and each iteration slices and computes prod/lcm/gcd over a window of size up to N. (More strictly, O(N^2 * log M) where M is the maximum value in nums, if accounting for GCD/LCM operations.)
        - Space Complexity: O(N), due to slicing nums[left:right] which creates a temporary list of size up to N.
        """
        left = 0
        right = 2
        longest = 2

        while right <= len(nums):
            subarray = nums[left:right]
            if math.prod(subarray) == math.lcm(*subarray) * math.gcd(*subarray):
                longest = max(longest, right - left)
                right += 1
            else:
                left += 1

        return longest
