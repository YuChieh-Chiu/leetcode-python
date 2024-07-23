class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        """
        thought process:
        - this is a sorting problem with the following sorting principles:
            (1) sort by the frequency of the numbers in `ascending` order.
            (2) if frequencies are the same, sort by the numerical value in `descending` order.
        - there are multiple sorting algorithms we could use; here I choose to use a simple `dict` for sorting because:
            - a `dict` can easily count frequencies.
            - a `dict` allows for straightforward implementation of two-layer sorting.
        - therefore, we can follow these steps:
            (1) create an empty `dict`.
            (2) iterate through `nums` and add each number to the `dict`. If the number is already in the `dict`, increment its frequency by 1. If the number is not in the `dict`, set its frequency to 1.
            (3) sort the `dict` according to the problem's sorting principles.
            (4) construct the final output from the `dict`'s keys and values.
        """
        sort_nums = dict()
        output = []
        for num in nums:
            if num in sort_nums:
                sort_nums[num] += 1
            else:
                sort_nums[num] = 1
        sort_nums = sorted(sort_nums.items(), key=lambda item: (item[1], -item[0]), reverse=False) # after sorted, it would be `list`
        for (num, freq) in sort_nums:
            output.extend([num]*freq)
        return output
