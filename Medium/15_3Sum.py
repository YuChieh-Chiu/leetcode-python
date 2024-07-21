class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        thought:
        - our goal is to iterate through the entire list to find all unique combinations of three values that sum to 0.
            - note: The order of the output and the order of the triplets do not affect the result (important).
            - note: Triplet combinations must be unique.
        - we can try to sort the list in ascending order first, and then iteratively update the triplet range to find the required triplets.
        - therefore, we can follow these steps:
            (1) sort the list in ascending order.
            (2) iterate through the entire list and perform the following actions:
                - if the value at position `i` is the same as the value at position `i-1`, it means the next operation would be a duplicate, so we skip to the next position `i+1` to avoid duplicate actions.
                - define `left_pointer = i+1` (the value immediately to the right of `i`) and `right_pointer = numsLen-1` (the last value in the list).
                - check if the sum of the values at `i`, `left_pointer`, and `right_pointer` equals 0.
                    - = 0: move both pointers inward to check for other combinations that also sum to 0, but skip over values that are duplicates of the current `left_pointer` and `right_pointer`.
                    - > 0: move the `right_pointer` to the left to check for other combinations that also sum to 0.
                    - < 0: move the `left_pointer` to the right to check for other combinations that also sum to 0.
                - repeat this process until the two pointers overlap, then move to the next position `i+1`.
            - Nnote: Here we use the `two pointers` algorithm. (left right pointers)
        """
        nums = sorted(nums)
        output = []
        numsLen = len(nums)
        for i in range(numsLen):
            if i > 0 and nums[i] == nums[i-1]: # no need to check the same leftmost border again
                continue
            left_pointer = i + 1
            right_pointer = numsLen - 1
            while left_pointer < right_pointer:
                summation = nums[i] + nums[left_pointer] + nums[right_pointer]
                if summation == 0:
                    output.append([nums[i], nums[left_pointer], nums[right_pointer]])
                    while left_pointer < right_pointer:
                        if nums[left_pointer] == nums[left_pointer+1]:
                            left_pointer += 1
                        else:
                            break
                    while left_pointer < right_pointer:
                        if nums[right_pointer] == nums[right_pointer-1]:
                            right_pointer -= 1
                        else:
                            break
                    left_pointer += 1
                    right_pointer -= 1
                elif summation < 0:
                    left_pointer += 1
                else:
                    right_pointer -= 1
        return output
