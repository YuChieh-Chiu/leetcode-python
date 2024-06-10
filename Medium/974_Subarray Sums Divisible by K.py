class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        """
        thought:
        - we want to know the number of non-empty sub-arrays that have a sum divisible by `k`, which means we want to do `interval summation` and `search for the interval which is multiple of k`
        - we need `prefix sum` and `search` combination
        - there are two situations that the sum of interval would be divisible by `k`
            (1) when the remainder appears more than twice, any two positions of the remainder can form an interval divisible by `k`
            (2) if nums[i] % k == 0, then nums[i] can form an interval divisible by `k` on its own
        """
        d_cnt = {0:0} # how many times that `d` shows up
        cnt = 0 # number of non-empty sub-arrays
        for i in range(len(nums)):
            if i == 0: # no `i-1`
                pass
            else:
                nums[i] += nums[i-1] # prefix_sum
            remainder = (nums[i]) % k # `division` version of prefix_sum
            if remainder in d_cnt:
                d_cnt[remainder] += 1
            else:
                d_cnt[remainder] = 1
        # situation (1)
        for (_,v) in d_cnt.items():
            cnt += (v * (v-1)) // 2
        # situation (2)
        cnt += d_cnt[0]
        return cnt
