class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        """
        Thought:
        - Goal:  
            - Return the maximum value obtained from all valid triplets of indices (i, j, k).  
        - Constraints:  
            1. i < j < k 
            2. The value for each triplet is calculated as:  
                max((nums[i] - nums[j]) * nums[k], 0)
        - Steps:  
            1. Initialize a variable `maxTriplet` to store the maximum computed value.
            2. Use a triple-nested loop to iterate over all valid triplets (i, j, k), where i < j < k, and compute the corresponding value.  
            3. Return `maxTriplet` as the result.
        """

        maxTriplet = 0

        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    maxTriplet = max(maxTriplet, (nums[i] - nums[j]) * nums[k])

        return maxTriplet
