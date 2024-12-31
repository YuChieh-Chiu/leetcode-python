class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        Thought of Method 1:
        - Idea:
            - Based on the problem description, we understand that after repeatedly smashing the two heaviest stones, we will eventually be left with either no stone or one stone.
            - If no stones remain, we return 0; otherwise, we return the weight of the last remaining stone.
        - Steps:
            1. While the list `stones` contains more than one stone, repeat the following steps:
                (1) Sort the list in descending order to identify the two heaviest stones.
                (2) Compare their weights:
                    - If the weights are unequal, append the absolute difference of their weights to `stones`.
                (3) Remove the first two elements from the list `stones`.
            2. If the list `stones` becomes empty, return 0.
            3. Otherwise, return the weight of the last remaining stone.
        """
        while len(stones) > 1:
            stones = sorted(stones, reverse=True)
            first, second = stones[0], stones[1]
            if first != second:
                stones.append(abs(first-second))
            stones = stones[2:]

        if len(stones) == 0:
            return 0
        else:
            return stones[0]
