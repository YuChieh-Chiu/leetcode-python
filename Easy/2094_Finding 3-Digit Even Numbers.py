class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        """
        Thought:
        - Goal: Find all unique three-digit even numbers that can be formed from `digits`, 
          and return them in sorted ascending order.
        - Idea:
            - Three-digit rule: the last digit must be even, and the first digit must be non-zero.
            - The returned sequence should be a sorted list of unique integers.
        - Steps:
            1. Create a set `three_digits_even` to hold unique three-digit even numbers.
            2. Use three nested loops to pick each digit in turn, checking the rules:
                - At each level, copy the current list of remaining digits and remove the chosen one to avoid reusing the same value.
                - In the first loop, skip if the digit is 0 (no leading zero allowed).
                - In the third loop, check if the digit is even; if so, combine the three digits into an integer and add it to the set.
            3. Return a sorted list converted from the set.
        - Time Complexity: O(n^3)
        - Space Complexity: O(n)
        """

        three_digits_even = set()

        for first_digit in set(digits):
            # Skip leading zero
            if first_digit == 0:
                continue
            digits_minus1 = digits.copy()
            digits_minus1.remove(first_digit)

            for second_digit in set(digits_minus1):
                digits_minus2 = digits_minus1.copy()
                digits_minus2.remove(second_digit)

                for third_digit in set(digits_minus2):
                    # Only even units digit
                    if third_digit % 2 == 0:
                        # Build the number and add to set
                        three_digits_even.add(
                            first_digit * 100 + second_digit * 10 + third_digit
                        )

        return sorted(three_digits_even)
