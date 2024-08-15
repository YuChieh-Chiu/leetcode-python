class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        """
        thought:
        - from the problem description, we understand the following:
           - we start with no change, so we should initialize a `choices` dictionary with `{5:0, 10:0, 20:0}`.
           - each customer buys one lemonade and pays with either a $5, $10, or $20 bill. Therefore, we may need to give back $0, $5, or $15 as change.
        - our goal is to determine if we can give the correct change to every customer.
        - we can achieve this by following these steps:
           (1) initialize `choices` with `{5:0, 10:0, 20:0}`.
           (2) traverse through the `bills` list and for each bill, do the following:
               - add the bill to `choices`.
               - subtract 5 from the bill to determine the amount of change needed.
               - check if we can provide the correct change. If not, return `False`; otherwise, continue:
                   # if `change_needed` is $0, continue.
                   # if `change_needed` is $5, check if we have at least one $5 bill.
                   # If `change_needed` is $15, check if we have at least one $10 bill and one $5 bill, or at least three $5 bills.
        """
        choices = {5:0, 10:0, 20:0}
        for bill in bills:
            choices[bill] += 1
            change_needed = bill - 5
            if change_needed == 0:
                continue
            elif change_needed == 5:
                if choices[5] == 0:
                    return False
                choices[5] -= 1
            else:
                if (choices[10] > 0) & (choices[5] > 0):
                    choices[10] -= 1
                    choices[5] -= 1
                elif (choices[10] == 0) & (choices[5] > 2):
                    choices[5] -= 3
                else:
                    return False
        return True
