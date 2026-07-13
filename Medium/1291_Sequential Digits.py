class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        """
        Thought:
        - Goal: Find all integers in the range [low, high] inclusive that have sequential digits, sorted in ascending order.
        - Idea: The total number of sequential digit combinations is very small (only 36 possible numbers between 10 and 10^9). Instead of checking every single number in the range, we can systematically generate all possible sequential digits based on the digit lengths of 'low' and 'high' using the base sequence "123456789".
        - Steps:
            1. Determine the minimum length (low_digit) and maximum length (high_digit) of the target numbers.
            2. Iterate through each possible length from low_digit to high_digit.
            3. For each length, slide a window across the string "123456789" to generate sequential numbers.
            4. Convert the substring to an integer. If it falls within [low, high], append it to the result list. Break early if the generated number exceeds 'high'.
        - Time Complexity: O(1). The total number of valid sequential digits is bounded by a constant (maximum 36 combinations), making the execution time independent of the input values.
        - Space Complexity: O(1). The output list stores at most 36 integers, and the extra variables used for string slicing consume a fixed, minimal amount of memory.
        """
        sample = "123456789"
        sequential_digits_list = []
        
        low_digit = len(str(low))
        high_digit = len(str(high))
        
        for digit in range(low_digit, high_digit + 1):
            for i in range(10 - digit):
                num = int(sample[i : i + digit])                
                if num > high:
                    break
                if num >= low:
                    sequential_digits_list.append(num)
                    
        return sequential_digits_list
