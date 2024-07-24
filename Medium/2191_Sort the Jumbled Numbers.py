class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        """
        thought:
        - notice the constraints given in the problem:
            (1) `mapping` is a 0-indexed array.
            (2) the sorting result should be in non-decreasing order, and if the mapped values are the same, the relative order should be preserved.
            (3) the result should output the original values from `nums`.
        - our goal is to transform each value in `nums` according to the `mapping` rules and then sort based on the transformed values.
        - therefore, we can follow these steps:
            (1) transform the values in `nums` according to the `mapping` rules.
            (2) sort the transformed values based on the constraints given in the problem.
                - there are many sorting algorithms that could be used. Here, we'll simply use a dictionary for sorting for the following reasons:
                    1. it conveniently allows us to output the original values directly.
                    2. this problem requires two levels of sorting criteria (numerical value and relative position), and using a dictionary facilitates achieving both levels easily.
            (3) output the "original numbers" after sorting.
        """
        nums_ids_labels = []
        for idx, num in enumerate(nums):
            label = ""
            for char in str(num):
                label += str(mapping[int(char)])
            nums_ids_labels.append((num, idx, int(label)))
        nums_ids_labels = sorted(nums_ids_labels, key=lambda x: (x[2], x[1]))
        nums = [item[0] for item in nums_ids_labels]
        return nums
