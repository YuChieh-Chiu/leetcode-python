class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        """
        thought:
        - we want to find whether there exists `3 consecutive odds` SUBARRAY in `arr`
        - we can use `sliding window` which follows the RULES below:
            (1) the window size = 3
            (2) if even number shows, the window size should be initialized to 0
        """
        size = 0
        for i in arr:
            if i % 2 != 0: # odd number
                size += 1
            else:
                size = 0
            if size == 3:
                return True
        return False
