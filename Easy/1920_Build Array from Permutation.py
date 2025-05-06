class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        """
        Thought:
        - Goal:
            - Given a zero-based permutation `nums` containing distinct integers from 0 to nums.length - 1,
            construct an array `ans` such that ans[i] = nums[nums[i]] for all valid indices i.
        - Key Point:
            - ans[i] = nums[nums[i]]
        - Approaches:
            1. Intuitive Approach (Space Complexity: O(n)):
                - Create a new array `ans`.
                - Traverse the input array `nums` and for each index `i`, append nums[nums[i]] to `ans`.
            2. In-Place Encoding Approach (Space Complexity: O(1)):
                - Modify `nums` in-place to encode both the original and new values in a single integer.
                - Use the formula: nums[i] += n * nums[nums[i]]
                    - Here, `n` is the array length and greater than any value in `nums`.
                    - nums[nums[i]] % n ensures we retrieve the original unmodified value.
                - After the encoding step, retrieve the final result by dividing each value by `n`: nums[i] //= n
        - Steps (O(n) Space):
            1. Initialize an empty array `ans`.
            2. For each index `i` in `nums`, compute nums[nums[i]] and append it to `ans`.
        - Steps (O(1) Space):
            1. Let `n` be greater than length of `nums`.
            2. For each index `i`, update: nums[i] += n * (nums[nums[i]] % n)
            3. After the loop, update each element: nums[i] //= n
        """

        # space complexity: O(1)
        for i, num in enumerate(nums):
            val = nums[nums[i]] % 1e4
            val *= 1e4
            nums[i] = nums[i] + val

        for i, num in enumerate(nums):
            nums[i] = int(num // 1e4)

        return nums

        # # space complexity: O(n)
        # ans = []
        
        # for num in nums:
        #     ans.append(nums[num])

        # return ans
