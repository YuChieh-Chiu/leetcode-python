class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        """
        Thought:
        - Goal:  
            - Return the length of the longest nice subarray given an array `nums` consisting of positive integers.  
        - Definition of a nice subarray:  
            - The bitwise AND of every pair of elements at different positions in the subarray must be equal to 0.  
            - Note that subarrays of length `1` are always considered nice, meaning that the minimum length is 1.  
        - Idea:  
            - For each element `x` we traverse, we only need to check the bitwise AND between `x` and each element in the current nice subarray.  
        - Steps:  
            1. Initialize two variables:  
                - `nice_start` as `-1`, representing the start position of the nice subarray.  
                - `max_length` as `1`, representing the minimum length of a nice subarray.  
            2. Traverse through `nums` starting from position 1:  
                - If `nice_start` equals `-1`, meaning that we have not found a nice subarray yet, we only need to compare the current element with the previous element:  
                    - If the bitwise AND of these two elements equals 0, we set `nice_start` to `i - 1`, representing the position of the previous element in the comparison.  
                - Otherwise, we compare the current element with every element in the nice subarray:  
                    - Each time we get a non-zero result between the current element and an element in the nice subarray, we reassign `nice_start` as `j + 1`, where `j` is the position of the compared element in the nice subarray.  
                    - At the end of the comparison, we use `max()` to check whether the length of the subarray from `nice_start` to the current position is longer than the current `max_length`, and update it accordingly.  
            3. Return `max_length`.  
        """
        nice_start = -1
        max_length = 1

        for i, num in enumerate(nums[1:], 1):
            if nice_start == -1:
                if nums[i-1] & num == 0:
                    nice_start = i - 1
            else:
                for j, num2 in enumerate(nums[nice_start:i], nice_start):
                    if num2 & num != 0:
                        nice_start = j + 1
                max_length = max(i - nice_start + 1, max_length)
                
        return max_length
