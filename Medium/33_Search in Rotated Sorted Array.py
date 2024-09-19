class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        thought:
        - our goal is to search for the integer `target` in the List[int] `nums` with O(log n) runtime complexity.
        - based on the problem description, we can infer the following:
            (1) `nums` is originally sorted in ascending order with distinct values, meaning we are searching for `target` in a distinct, sorted list. Therefore, Binary Search can be used to achieve O(log n) time complexity.
            (2) however, `nums` might be rotated at an unknown pivot index, so we need to account for the rotation when searching.
        - therefore, the steps are as follows:
            (1) first, restore the list to its original ascending order using `sorted()`.
            (2) then, apply Binary Search to find the target within the sorted list:
                - Binary Search: Recursively compare `target` to the middle value of the sublist, checking whether `target` is greater, less than, or equal to the middle value.
            (3) if the middle value equals `target`, return its index; otherwise, return -1.
                - Note: since the list was initially rotated, we need to map the index found in the sorted list back to its original position in the rotated list.
        """
        # step (1)
        sorted_nums = sorted(nums)
        # step (2)
        left = 0
        right = len(sorted_nums)-1
        while left <= right:
            middle = (left+right)//2
            val = sorted_nums[middle]
            if val < target:
                left = middle + 1
            elif val > target:
                right = middle - 1
            else:
                return nums.index(val)
        # step (3)
        return -1 
