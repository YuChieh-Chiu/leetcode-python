class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        thought:
        - our goal is to search for the integer `target` in a sorted array `nums`. If we find the target, we should return its index; otherwise, we should return the index where it would be inserted if not found.
        - Binary Search is the algorithm that can search for the target in a sorted array with O(log n) runtime complexity, so we will use it to solve the problem.
        - the key point is that when the target is not found, we should return the index where it would be inserted. This means finding the index of the closest value that is greater than the target.
        - therefore, we follow these steps:
            (1) define the variables `left` and `right` to represent the left and right boundaries of the sublist of the sorted array.
            (2) apply Binary Search to find the target within the sorted array:
                - Binary Search: Repeatedly compare the `target` to the middle value of the sublist, checking whether `target` is greater than, less than, or equal to the middle value.
            (3) if the middle value equals `target`, return its index; otherwise, return `left` which represent the closeset value that is greater than the target.
        """
        left = 0
        right = len(nums)-1
        while left <= right:
            middle = (left+right)//2
            val = nums[middle]
            if target > val:
                left = middle + 1
            elif target < val:
                right = middle - 1
            else:
                return middle
        return left
