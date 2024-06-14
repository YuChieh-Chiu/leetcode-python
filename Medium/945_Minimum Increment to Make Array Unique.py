class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        """
        thought:
        - we need to make every value in array unique
        - if length of array == 1, we can just return array
        - if length of array != 1, because value in array >= 0, do the following steps:
            (1) create a new array with length == (max value of array) in array
            (2) count the number of each value and add the number to the new array
            (3) traverse the new array and calculate the moves
        """
        moves = 0 # initialize `moves`
        new_length = max(nums)+1 # get the length of `cnt_array`
        if len(nums) == 1:
            return moves
        cnt_array = [0] * (new_length+1) # create `cnt_array` with all value == 0 and length == new_length+1
        for num in nums: # count number of each value
            cnt_array[num] += 1
        for i in range(min(nums), new_length): 
            # traverse from the first non-zero value to the end-1 because:
            # 1. the zero value before the first non-zero value is useless while we can only increment
            # 2. we need index i+1 as below so we cannot traverse to the very end
            if cnt_array[i] > 1: # greedy moves : if the number of value > 1, we moves the excess part to the next index
                current_moves = cnt_array[i] - 1
                cnt_array[i+1] += current_moves
                cnt_array[i] -= current_moves
                moves += current_moves
        # if we do greedy moves through array and still need to increment at the very end of array:
        # just add the sum of those excess part into `moves`
        if cnt_array[-1] > 1:
            max_steps = cnt_array[-1] - 1
            moves += ((1 + max_steps)*max_steps)//2
        return moves
