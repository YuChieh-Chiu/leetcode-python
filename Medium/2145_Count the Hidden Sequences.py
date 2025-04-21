class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        """
        Thought:
        - Goal: Given a list of differences between consecutive elements of a hidden array, a lower bound, and an upper bound, find the number of possible original arrays that satisfy these conditions.
        - Idea:  
            - The key insight is that once we choose the first element of the hidden array, all other elements are determined by the given differences.
            - We can construct the minimum possible hidden array by setting its first element to the lower bound.
            - By sorting the constructed array, we can identify its minimum and maximum values.
            - The number of possible arrays will depend on how much we can shift the first element up while keeping all elements within the allowed range.
        - Steps:  
            1. Construct the minimum possible hidden array by setting the first element to `lower` and computing subsequent elements using the given differences.
            2. Sort this array to find its minimum and maximum values.
            3. Check if the maximum value exceeds `upper`. If yes, return 0 as no valid array exists.
            4. Otherwise, calculate how much we can increase the first element:
                - Maximum increase = `upper - max_value_in_array`
                - This gives us the highest possible value for the first element.
                - The total number of possible arrays is: `(highest_possible_first_element - lower + 1)`
                    - `highest_possible_first_element = base_case_first_element + maximum_increase`
            5. Return this count, ensuring it's not negative.
        - Time Complexity: O(n log n) due to the sorting operation
        - Space Complexity: O(n) for storing the constructed hidden array
        """
        min_possible_hidden = [lower]
        for i, diff in enumerate(differences):
            next_integer = min_possible_hidden[i] + diff
            min_possible_hidden.append(next_integer)
        
        min_possible_hidden = sorted(min_possible_hidden)

        if min_possible_hidden[-1] > upper:
            return 0
        else:              
            return max(min_possible_hidden[0] + (upper - min_possible_hidden[-1]) - lower + 1, 0)
