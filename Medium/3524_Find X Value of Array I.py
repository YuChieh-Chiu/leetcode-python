class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        """
        Thought:
        - Goal:
            Find the number of non-empty subarrays whose product modulo k equals x, for all 0 <= x <= k - 1.
        - Idea:
            Removing a prefix and suffix from the array such that the remaining elements are non-empty
            is equivalent to choosing any non-empty contiguous subarray. We can use dynamic programming:
            maintain a frequency table of remainder values for all subarrays ending at the current index.
            For each new element `num`, extending any existing subarray ending at the previous index
            multiplies its remainder by `num % k`. Additionally, `num` can start a new subarray of length 1.
        - Steps:
            1. Initialize `result` of size `k` with zeros to accumulate subarray counts for each remainder.
            2. Maintain `prev_dp` of size `k`, tracking counts of remainders for subarrays ending at the previous position.
            3. Iterate through each `num` in `nums`:
                a. Initialize `curr_dp` of size `k`.
                b. Account for the single-element subarray `[num]` by incrementing `curr_dp[num % k]`.
                c. For each non-zero count in `prev_dp[r]`, add that count to `curr_dp[(r * num) % k]`.
                d. Add the counts in `curr_dp` to `result`.
                e. Set `prev_dp = curr_dp`.
            4. Return `result`.
        - Time Complexity:
            O(n * k), where n is the length of `nums` and k is the divisor.
        - Space Complexity:
            O(k), as we only maintain DP arrays and the result array of size k.
        """
        result = [0] * k
        prev_dp = [0] * k

        for num in nums:
            curr_dp = [0] * k
            curr_rem = num % k

            curr_dp[curr_rem] += 1

            for r in range(k):
                if prev_dp[r] > 0:
                    new_r = (r * curr_rem) % k
                    curr_dp[new_r] += prev_dp[r]

            for r in range(k):
                result[r] += curr_dp[r]

            prev_dp = curr_dp

        return result
