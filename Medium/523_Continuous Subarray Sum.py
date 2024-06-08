class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        thought:
        - we want to know whether there exists a sub-array that the sum of it is multiple of `k`, which means we want to do `interval summation` and `search for the multiple of k`
        - we need `prefix sum` and `search` combination
        reference:
        - the idea of the following code came from the reference below
            ``` reference
            - author : bangye wu
            - article url link : https://hackmd.io/@bangyewu/rJRpH9dhh#前綴與後綴
            ```
        """
        # set `sentinel`
        # IMPORTANT. use `SET` instead of `LIST` here because the time complexity of running lookup `x in set` is O(1) while the time complexity of running lookup `x in list` is O(n)
        exist_remainder = {0}
        prefix_sum_remainder = [nums[0]%k]
        for i in range(1, len(nums)):
            # the remainder of sum(1~m) = (the remainder of sum(1~(m-1)) + nums[m]) % k
            d = (prefix_sum_remainder[i-1] + nums[i])%k
            prefix_sum_remainder.append(d) 
            # if remainder `d` appears again, it means that the total sum of intervals between the indices where remainder `d` showed up last time and where it shows up this time can be divided by `k` with a remainder of 0.
            if d in exist_remainder:
                return True
            else:
                exist_remainder.add(prefix_sum_remainder[i-1])
        return False
