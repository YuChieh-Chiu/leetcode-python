class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        thought:
        - from the problem description, we know the constraints as follows:
            (1) we need to remove all occurrences of `val` from the array `nums`.
            (2) we need to remove `val` in place.
            (3) but we only care about first k elements in `nums`.
            - therefore, we can follow these steps:
                (1) define a `pointer`:
                    - `pointer`: Points to the index currently being checked.
                (2) define `k` to record the number of elements not equal to `val`.
                (3) traverse the array and check the following conditions:
                    - If `nums[pointer]` != `val`:
                        - Increment `k`.
                        - Increment the `pointer`.
                    - else:
                        - Delete `nums[pointer]`.
                        - Update the length of `nums`.
        """
        pointer = 0
        k = 0
        while pointer < len(nums):
            if nums[pointer] != val:
                k += 1
                pointer += 1
            else:
                del nums[pointer]
        return k
