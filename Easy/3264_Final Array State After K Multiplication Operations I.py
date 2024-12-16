import heapq
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        """
        Thought:
        - Problem Description:
            - The task requires performing `k` operations on the list `nums`. In each operation:
                - Identify the minimum value `x` in `nums`. If there are multiple occurrences of `x`, choose the first one.
                - Replace the selected minimum value `x` with `x * multiplier`.
        - Concept:
            - To efficiently find the minimum value `x` in `nums`, we can use a Min Heap data structure.
            - The operations can be simulated step by step using a simple algorithm.
        - Steps:
            1. Initialize the Min Heap:
                - Use the `heapify()` function to transform `nums` into a min heap.
            2. Perform `k` operations:
                - For each operation:
                    1. Use `heappop()` to extract the smallest value, `min_value`, from the heap.
                    2. Multiply `min_value` by `multiplier` to compute the new value, `new_value`.
                    3. Replace the first occurrence of `min_value` in the original `nums` list with `new_value`.
                    4. Use `heappush()` to insert `new_value` back into the heap.
            3. Return the Updated List:
                - After completing all operations, return the modified `nums` list.
        """
        heap_nums = nums[:]
        heapq.heapify(heap_nums)
        for _ in range(k):
            min_value = heapq.heappop(heap_nums)
            new_value = min_value * multiplier
            nums[nums.index(min_value)] = new_value
            heapq.heappush(heap_nums, new_value)
        return nums
