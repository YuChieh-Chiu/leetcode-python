class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        thought:
        - from the problem description, we know the constraints as follows:
            (1) we need to remove duplicates from a non-decreasing order array.
            (2) we need to remove the duplicates in place.
        - this means that we have to use the `two-pointer` algorithm to solve this problem.
        - therefore, we can follow these steps:
            (1) define two pointers: `left_pointer` and `right_pointer`.
            (2) define `k` to record the number of unique values.
            (3) traverse the array and check the following points:
                - if `left_pointer` equals `right_pointer`:
                    # if `right_pointer` smaller than `size`, continue to find the value that is not equal to `nums[left_pointer]`.
                    # if `right_pointer` equals to `size`, it means that from `left_pointer` to `size`, the values are all the same, so we need to remove them, get the length of `nums` after deleting and increment `left_pointer`.
                - if `left_pointer` does not equal `right_pointer`:
                    # remove the subarray from `left_pointer + 1` to `right_pointer - 1`, which contains duplicates.
                    # get the length of `nums` after deleting.
                    # increment `left_pointer` to check the next value in `nums`.
                    # increment `k` by 1.
                    # break and enter a new iteration of the loop.
        """
        k = 1
        left_pointer = 0
        size = len(nums)
        while left_pointer < size-1:
            for right_pointer in range(left_pointer+1, size):
                if nums[left_pointer] != nums[right_pointer]:
                    del nums[left_pointer+1:right_pointer]
                    size = len(nums)
                    left_pointer += 1
                    k += 1
                    break
                else:
                    if right_pointer == size-1:
                        del nums[left_pointer+1:size]
                        size = len(nums)
                        left_pointer += 1
        return k
