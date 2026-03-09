class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Thought:
        - Goal: Find the constant integer 'x' that was added to every element in nums1 to produce nums2.
        - Idea: Since every element is shifted by the same value, the difference between any corresponding statistics (like minimum, maximum, or sum) of the two arrays will yield 'x'.
        - Steps:
            1. Identify the minimum element in nums1.
            2. Identify the minimum element in nums2.
            3. Calculate the difference: min(nums2) - min(nums1).
        - Time Complexity: O(n), where n is the length of the arrays, as we only need a single pass to find the minimums.
        - Space Complexity: O(1) additional space.
        """
        return min(nums2) - min(nums1)
