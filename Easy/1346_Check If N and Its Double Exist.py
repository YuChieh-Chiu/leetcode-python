class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        """
        Thought:
        - Goal: Check if there exist two different indices `i` and `j` in the array such that `arr[i] == 2 * arr[j]`.
        - Idea: Use a Hash Set to keep track of the numbers we have seen so far. As we iterate through the array, we can look back in O(1) time to check if the current number's double or exact half already exists in the set.
        - Steps:
            1. Initialize an empty hash set named `seen`.
            2. Iterate through each integer `num` in the array `arr`.
            3. For each `num`, check if `num * 2` exists in `seen`.
            4. Also check if `num` is an even number AND `num // 2` exists in `seen`.
            5. If either condition is true, we found a valid pair. Return `True`.
            6. Otherwise, add `num` to `seen` and continue to the next number.
            7. If the loop completes without finding any valid pair, return `False`.
        - Time Complexity: O(N)
        - Space Complexity: O(N)
        """
        seen: set[int] = set()

        for num in arr:
            if (num * 2 in seen) or (num % 2 == 0 and num // 2 in seen):
                return True
            seen.add(num)
        
        return False
