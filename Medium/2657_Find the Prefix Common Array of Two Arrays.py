class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        """
        Thought:
        - Goal:
            - Return the prefix common array of A and B.
        - Definition:
            - The prefix common array is an array where the i-th element represents the count of numbers that are present at or before index i in both A and B.
        - Steps:
            1. Initialize variables:
                - prefix_sum: Tracks the count of numbers currently common between A and B.
                - prefix_sum_list: Stores the value of prefix_sum at each index from 0 to n.
                - prefix_a: Stores elements in A that are not yet matched in B.
                - prefix_b: Stores elements in B that are not yet matched in A.
            2. Iterate through A and B simultaneously:
                - If the elements at index i in A and B are equal, increment prefix_sum by 1.
                - Otherwise:
                    - If the element at index i in A exists in prefix_b, increment prefix_sum by 1 and remove the element from prefix_b (since it is now matched). Otherwise, add the element to prefix_a.
                    - If the element at index i in B exists in prefix_a, increment prefix_sum by 1 and remove the element from prefix_a (since it is now matched). Otherwise, add the element to prefix_b.
                    - Append the current value of prefix_sum to prefix_sum_list.
        - Return: 
            - prefix_sum_list.
        """

        prefix_sum = 0
        prefix_sum_list = []
        prefix_a = []
        prefix_b = []

        for a, b in zip(A, B):
            if a == b:
                prefix_sum += 1
            else:
                if a in prefix_b:
                    prefix_b.remove(a)
                    prefix_sum += 1
                else:
                    prefix_a.append(a)
                if b in prefix_a:
                    prefix_a.remove(b)
                    prefix_sum += 1
                else:
                    prefix_b.append(b)
            prefix_sum_list.append(prefix_sum)

        return prefix_sum_list
