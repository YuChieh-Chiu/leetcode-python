class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        """
        thought:
        - we want to find subarray in array, so we can use algorithm `Sliding Windows`
        - the RULE in sliding window that we should follow
            (1) if we don't encounter the k odd number yet, we should just keep going on
            (2) if we encounter the k odd number, but still not encounter the k+1 odd number, then THE SUBARRAY WHICH CONTAINS K ODD NUMBER ARE ALL `NICE SUBARRAY`
            (3) if we encounter the k+1 odd number, we should remove the first odd number
        """
        tot = 0
        odd_cnt = 0
        left_border = 0
        first_odd_index_in_window = -1
        for i, num in enumerate(nums):
            if num % 2 == 1: # odd_number
                if first_odd_index_in_window == -1:
                    first_odd_index_in_window = i
                odd_cnt += 1
            if odd_cnt > k:
                for j in range(left_border, i): # remove the first odd number
                    if nums[j] % 2 == 1:
                        left_border = j + 1
                        break
                for l in range(left_border, i+1): # get the index of first odd number in window
                    if nums[l] % 2 == 1:
                        first_odd_index_in_window = l
                        break
                odd_cnt -= 1
            if odd_cnt == k:
                tot += (first_odd_index_in_window - left_border + 1)
        return tot
