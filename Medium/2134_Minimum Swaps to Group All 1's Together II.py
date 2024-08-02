class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        """
        thought：
        - we know the definition of `swap` and `circular array`：
            - swap：taking two distinct positions in an array and swapping their values
            - circular array：an array where the first element and the last element are considered adjacent
        - to eliminate the circular property, we can append the array to itself
        - considering that a swap can eliminate a ZERO GAP between two ONEs, our target is to find the subarray with ALL ONEs and THE LEAST ZEROs instead of finding minimum swaps
        - therefore, we can follow these steps：
            (1) append the array to itself to eliminate the circular property
            (2) calculate the number of ONE and denote it as `all_ones`
            (3) use the `sliding window` technique to find the subarray with the following RULES：
                - the length of subarray should be equal to the number of ALL ONEs
            (4) find the `window` with the LEAST zeros to determine the answer for the minimum swaps
        """
        zeros = 0
        windows = 0
        left_open = 0
        min_swaps = 100000
        all_ones = nums.count(1) # get the number of ONE
        nums += nums
        for num in nums:
            if num == 0:
                zeros += 1
            windows += 1
            if windows > all_ones:
                if nums[left_open] == 0:
                    zeros -= 1
                windows -= 1
                left_open += 1
            if windows == all_ones:
                min_swaps = min(min_swaps, zeros)
        return min_swaps
