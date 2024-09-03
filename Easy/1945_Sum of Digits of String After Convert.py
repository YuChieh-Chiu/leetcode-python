class Solution:
    def getLucky(self, s: str, k: int) -> int:
        """
        thought:
        - from the problem description, we can infer the workflow of the `getLucky` function as follows:
            1. convert the string `s` into a series of integers by replacing each letter with its corresponding position in the alphabet.
            2. calculate the sum of all digits obtained in step 1.
            3. if `k` > 1, continue calculating the sum of all digits obtained in step 2, repeating this process `k` times in total (including the first calculation).
        - our goal is to define a workflow to implement the steps above.
        - therefore, we can proceed with the following steps:
            (1) define a variable `digits` to store all digits as a string.
            (2) map each letter to its corresponding integer using the formula `ord(char) - 96`.
                - for example, `ord('a') = 97` so `ord('a') - 96 = 1`.
            (3) use a loop to calculate the sum of all digits `k` times.
                in each iteration:
                - traverse all characters in `digits`.
                    - convert each character to an integer.
                    - calculate the sum of these integers.
                - convert the sum back to a string and store it in `digits`.
            (4) after completing the loop, convert `digits` to an integer and return it as the final result.
        """
        
        digits = ""
        for chr in s:
            digits += str(ord(chr) - 96)
        for i in range(k):
            sumOfDigits = 0
            for chr in digits:
                sumOfDigits += int(chr)
            digits = str(sumOfDigits)
        return int(digits)
