# METHOD 1
from heapq import *
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """
        thought:
        - we want to find subarray in array, so we can use algorithm `Sliding Windows`
        - the RULE in sliding window that we should follow is 「the absolute difference between any two elements of the sliding window is less than or equal to `limit`」, which means
            (1) if the absolute difference between the biggest/smallest element in sliding window and the element we add to the sliding window is less than or equal to `limit`, we can JUST ADD IT
            (2) if NOT, we should traverse sliding window to remove those elements that violate the RULE when we add new element
        - Note that if we need to get max and min value in sliding window by max() and min() each time, the time complexity is too high (O(n^2))
        - So we have to use `heap` to shorten the time complexity to O(nlog(n))
        """
        longest = 0
        window = []
        min_pq = []
        max_pq = []
        for i, num in enumerate(nums):
            window.append(num)
            heappush(min_pq, num)
            heappush(max_pq, num*(-1))
            if (max_pq[0]*(-1)-num > limit) | (num-min_pq[0] > limit):
                left_border = 0
                for j, w_num in enumerate(window):
                    if abs(w_num-num) > limit:
                        left_border = j+1
                if (len(window)-1) > longest:
                    longest = len(window)-1
                window = window[left_border:]
                while num-min_pq[0] > limit:
                    heappop(min_pq)
                while max_pq[0]*(-1)-num > limit:
                    heappop(max_pq)       
        if len(window) > longest:
            longest = len(window)
        return longest

# METHOD 2
from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """
        thought:
        - we want to find subarray in array, so we can use algorithm `Sliding Windows`
        - the RULE in sliding window that we should follow is 「the absolute difference between any two elements of the sliding window is less than or equal to `limit`」, which means
            (1) MAX - MIN <= limit
            (2) if MAX - MIN > limit, then we should compare index(MAX) vs. index(MIN)
                - index(MAX) < index(MIN): we should remove all left than index(MAX), include itself
                - index(MAX) > index(MIN): we should remove all left than index(MIN), include itself 
        - Note that if we need to get max and min value in sliding window by max() and min() each time, the time complexity is too high (O(n^2))
        - So we can try to use `monotonic deque` to much more shorten the time complexity to O(n)
        """
        longest = 0
        dq_max = deque() # store index in monotonic descending order
        dq_min = deque() # store index in monotonic ascending order
        left_border = 0
        for i, num in enumerate(nums):
            if len(dq_max) > 0:
                while (len(dq_max) > 1) & (num >= nums[dq_max[-1]]):
                    dq_max.pop()
                if (num >= nums[dq_max[-1]]):
                    dq_max.pop()
            dq_max.append(i)
            if len(dq_min) > 0:
                while (len(dq_min) > 1) & (num <= nums[dq_min[-1]]):
                    dq_min.pop()
                if (num <= nums[dq_min[-1]]):
                    dq_min.pop()
            dq_min.append(i)
            while (nums[dq_max[0]] - nums[dq_min[0]]) > limit:
                if dq_max[0] < dq_min[0]: # the index of max value is smaller than the index of min value
                    left_border = dq_max[0] + 1
                    dq_max.popleft()
                else:
                    left_border = dq_min[0] + 1
                    dq_min.popleft()
            if (i-left_border+1) > longest:
                longest = (i-left_border+1)
        return longest
