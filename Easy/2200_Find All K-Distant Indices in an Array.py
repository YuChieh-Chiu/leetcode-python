class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        """
        Thought:
        - Goal: Return a list of all k-distant indices sorted in increasing order.
        - Definition: A k-distant index is an index i of nums for which there exists at least one index j such that |i - j| <= k and nums[j] == key.
        - Idea: When traversing each index i, check if the last index with value equal to key on the left side of index i (excluding index i) satisfies the condition, and simultaneously check if the nearest index with value equal to key on the right side (including index i) satisfies the condition.
        - Steps:
            1. Initialize k_dist as an empty array to store qualifying indices, and positions l and r as negative infinity, where l is the last index with value equal to key up to position i, and r is the first index with value equal to key starting from position i.
            2. When traversing each index i:
                2-1. Check if r satisfies the definition (>i): if not, traverse nums[i:] to find an index with value equal to key, update r and break the loop. If not found, it means there are no more values equal to key starting from index i, so set r to infinity.
                2-2. Check if |l-i| or |i-r| is less than or equal to k, record indices that satisfy the condition and store them in k_dist.
                2-3. When num == key, it means l needs to be updated to maintain the definition that l is the leftmost last index with value equal to key when checking i+1.
            3. Return k_dist
        """
        k_dist = []
        l = float('-inf')
        r = float('-inf')

        for i, num in enumerate(nums):
            if r < i:
                for j, num_j in enumerate(nums[i:], i):
                    if num_j == key:
                        r = j
                        break
                if r < i: # no more index with value equals to `key` after index i-1
                    r = float('inf')

            if abs(l-i) <= k or abs(i-r) <= k:
                k_dist.append(i)

            if num == key:
                l = i # update `l` to `i` to be the latest index with value equals to `key` before i+1
        
        return k_dist
