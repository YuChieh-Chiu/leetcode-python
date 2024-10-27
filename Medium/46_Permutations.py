class Solution:
    def addon(self, nums: List[int], chosen: List[int], permutations: List[List[int]]):
        # If the length of `nums` equals the length of `chosen`, this means we have a complete permutation, which we can add to `permutations`
        if len(nums) == len(chosen):  
            permutations.append(chosen[:])
            return
        # Traverse each element in the array `nums`
        for num in nums:
            # If the integer `num` is already in the list `chosen`, skip this iteration
            if num in chosen:
                continue
            # Recursively continue to build the permutation
            else:
                chosen.append(num)
                self.addon(nums, chosen, permutations)
                # IMPORTANT: Backtracking—remove the last added integer `num` to explore alternative integers
                chosen.pop()  
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        thought:
        - Objective: 
            - Return all possible permutations for a given array `nums` of distinct integers.
        - Thinking Process:
            - Generate all possible permutations.
            - Use exhaustive search with backtracking to efficiently explore each permutation path.
            - Key concepts:
                - For loop: iterate through each integer in `nums`.
                - Recursion: recursively call the function, avoiding integers already in the `chosen` list.
        - Steps:
            (1) Initialize `permutations` to store all potential permutations.
            (2) Define a helper function `addon` to handle the recursive logic.
            (3) Call `addon` to execute the recursive permutation building.
        """
        permutations = []  # Store all possible permutations
        self.addon(nums, [], permutations)
        return permutations
