import math
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        """
        thought:
        - from the problem description, we have the following information:
            1. the 6-sided die is numbered from 1 to 6.
            2. the total value is calculated as the average value (`mean`) multiplied by the total number of rolls (`n` + `len(rolls)`).
            3. `mean` is an integer.
        - our goal is to return one possible list of missing rolls.
        - therefore, we can follow these steps:
            (1) initialize a list variable `output` to store the result.
            (2) calculate the total value of the missing rolls by multiplying `mean` by (`n` + `len(rolls)`) and then subtracting `sum(rolls)`.
            (3) iteratively determine each value of the missing rolls, following these rules:
                - each value of the missing rolls must be between 1 and 6.
                - ensure that `n` is reduced to zero, indicating that all missing rolls have been determined.

        """     
        output = []   
        remaining = mean * (n + len(rolls)) - sum(rolls)
        while True:
            dice = math.ceil(remaining / n)
            if (dice > 6) | (dice < 1): # cannot generate
                return []
            else:
                if n > 1:
                    output.append(dice)
                    remaining -= dice
                    n -= 1
                else:
                    output.append(remaining)
                    return output
