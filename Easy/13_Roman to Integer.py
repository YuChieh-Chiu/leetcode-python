class Solution:
    def romanToInt(self, s: str) -> int:
        """
        thought:
        - from the problem statement, we can infer the following constraints:
            - 1 <= integer <= 3999
            - basic Roman numerals only include I, V, X, L, C, D, M. All possible integers in the problem are composed of these Roman numerals.
            - the way Roman numerals combine to form an integer is that numerals corresponding to smaller integers are placed before those corresponding to larger integers.
        - therefore, we can follow these steps:
            (1) create a variable `last` to record the previous Roman numeral, and a variable `output_int` to keep track of the total sum.
            (2) each time a new Roman numeral is added, convert it to its corresponding integer and add it to `output_int`. Then perform the following actions:
                - since the Roman numeral combination rule is that numerals corresponding to smaller integers are placed before those corresponding to larger integers, if the newly added Roman numeral corresponds to a larger integer than the previous one, it indicates a Roman numeral combination. In this case, subtract (the previous Roman numeral's corresponding integer) * 2 to adhere to the combination rule.
                    - e.g., IV = (V - I) = (I + V) - I * 2 = 4
                - update the `last` variable.
            (3) sum up the integers calculated in step (2).
        """
        r2i = {
            "": 0, "I": 1, "V": 5, "X":10, "L": 50, "C":100, "D":500, "M":1000
        } 
        last = 0
        output_int = 0
        for roman in s:
            int_i = r2i[roman]
            print(roman, int_i)
            output_int += int_i
            if int_i > last:
                output_int -= last*2
            else:
                pass
            last = int_i
        return output_int
