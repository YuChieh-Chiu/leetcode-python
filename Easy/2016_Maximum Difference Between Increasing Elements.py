class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        """
        Thought:
        - Goal: Find the maximum difference between nums[i] and nums[j] where 0<=i<j<n and nums[i]<nums[j]
        - Idea:
            - Use single pass to maintain the minimum value seen so far
            - For each position j, calculate difference with the minimum value from positions 0 to j-1
            - Only consider valid differences where nums[i] < nums[j] (i.e., current number > minimum)
            - Track the maximum valid difference throughout the traversal
            - Return -1 if no valid pair exists (e.g., array is non-increasing)
        - Steps:
            1. Initialize minVal to a nums[0] and maxDiff to -1
            2. Iterate through each number in the array
                - If current number > minVal, calculate difference and update maxDiff
                - Update minVal with the smaller of current minVal and current number
            3. Return the final maxDiff
        - Time Complexity: O(n) - single pass through the array
        - Space Complexity: O(1) - only using two variables
        """
        minVal = nums[0]
        maxDiff = -1

        for num in nums:
            if num > minVal:
                currentDiff = num - minVal
                maxDiff = max(maxDiff, currentDiff)
            minVal = min(minVal, num)
            
        return maxDiff
