class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        thought:
        - our goal is to find three numbers in `nums` that sum up to a value closest to the `target`.
        - this means we need to check every combination of three numbers in `nums` and see if their sum is closer to the `target` compared to previous sums.
        - note: To quickly check all pairs of numbers within a specific range, we can use the `two pointers` technique.
        - therefore, we can follow these steps:
            (1) sort `nums` in ascending order (let us know the move direction)
            (2) use a `for` loop to iterate through the sorted `nums`.
            (3) for each number, follow these rules:
                - if the current number is the same as the previous number, skip it (to avoid checking duplicate combinations).
                - if the current number is different from the previous number, execute the following `while` loop:
                    1. set the `left_pointer` to the leftmost position and the `right_pointer` to the rightmost position, and calculate the initial sum of the three numbers (three_sum).
                    2. compare the sum (three_sum) with the `target`:
                        - if three_sum > target: move the `right_pointer` to the left.
                        - if three_sum < target: move the `left_pointer` to the right.
                        - if three_sum == target: directly return `target`.
                    3. after each comparison, both pointers move inward. If the new three_sum is closer to the `target`, update the result; otherwise, the result remains unchanged.
                    4. when the two pointers meet, end the loop and proceed to the next number.
            (4) finally, return the sum that is closest to the `target`.
        """
        nums = sorted(nums)
        numsLen = len(nums)
        nearest = 100000
        for i in range(numsLen):
            if (i >= 1) & (nums[i] == nums[i-1]):
                continue
            left_pointer = i+1
            right_pointer = numsLen-1
            while left_pointer < right_pointer:
                three_sum = nums[i] + nums[left_pointer] + nums[right_pointer]
                if three_sum > target:
                    right_pointer -= 1
                elif three_sum < target:
                    left_pointer += 1
                else:
                    return target
                if abs(three_sum-target) < abs(nearest-target):
                    nearest = three_sum
        return nearest
