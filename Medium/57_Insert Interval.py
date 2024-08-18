class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        thought:
        - from the problem description, we can infer the following:
            - since `end` is greater than `start`, we don't need to iterate through `intervals` from the beginning.
            - if `newInterval` overlaps with any interval in `intervals`, they should be merged into a new interval.
        - therefore, we can follow these steps:
        (1) check if `intervals` is empty; if so, return [newInterval].
        (2) create variables `inserted_intervals` to store the intervals after insertion and `overlap` to determine if there is any overlap between `newInterval` and an interval.
        (3) iterate through `intervals` using a for loop:
            - if the upper bound of an interval is smaller than `newInterval[0]`, it means there is no overlap.
            - if the lower bound of an interval is greater than `newInterval[1]`, it also means there is no overlap.
            - otherwise, it means there is an overlap.
                - if the variable `overlap` is True, it means we've encountered an overlap and only need to update the upper bound of the overlapping interval.
                - otherwise, it means we've just encountered an overlap, and we should merge the minimum and maximum values of `interval` and `newInterval` into `inserted_intervals`.
                    - also, we should now set the variable `overlap` to True.
        (4) after the for loop, we should check if we've encountered an overlap or not. If not, it means `newInterval` has not been inserted yet.
            - we need to iterate through `intervals` and find the interval with a lower bound greater than the upper bound of `newInterval`, and then insert `newInterval` at that index.
            - if we don't find any interval that meets the above condition, it means `newInterval` should be at the end of `inserted_intervals`, so just append it.
        """
        if intervals == []:
            return [newInterval]
        inserted_intervals = []
        overlap = False
        for interval in intervals:
            lower, upper = interval
            if (upper < newInterval[0]) | (lower > newInterval[1]):
                inserted_intervals.append(interval)
            else:
                if overlap:
                    inserted_intervals[-1][1] = max(upper, newInterval[1])
                else:
                    inserted_intervals.append([min(lower, newInterval[0]), max(upper, newInterval[1])])
                    overlap = True
        if not overlap:
            for i, interval in enumerate(intervals):
                lower, _ = interval
                if lower > newInterval[1]:
                    inserted_intervals.insert(i, newInterval)
                    return inserted_intervals
            inserted_intervals.append(newInterval)
        return inserted_intervals
