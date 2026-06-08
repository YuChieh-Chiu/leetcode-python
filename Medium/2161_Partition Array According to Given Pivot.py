class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        """
        Thought:
        - Goal: Rearrange `nums` so elements are grouped by: [less than pivot, equal to pivot, greater than pivot], while maintaining their original relative order.
        - Idea (Evolution): 
            1. Initial thought: Use `insert(cnt, num)` for smaller elements. However, this leads to O(n^2) complexity because `insert` in a list is an O(n) operation in Python.
            2. Improved strategy: Use a partitioning approach. Create three separate lists to collect elements in a single pass. This ensures stability (relative order) and optimizes performance to linear time.
        - Steps:
            1. Initialize three empty lists: `less`, `equal`, and `greater`.
            2. Iterate through each number in the input `nums`.
            3. Append the number to the corresponding list based on its comparison with `pivot`.
            4. Concatenate and return the lists in the required order.
        - Time Complexity: O(n), where n is the length of `nums`. Each element is visited exactly once.
        - Space Complexity: O(n), to store the elements in the new lists.
        """
        less = []
        equal = []
        greater = []

        for num in nums:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                greater.append(num)

        # Python 的列表拼接操作高效且能保持加入時的順序
        return less + equal + greater
