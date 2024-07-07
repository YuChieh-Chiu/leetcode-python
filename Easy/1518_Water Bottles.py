class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        """
        thought:
        - every `numExchange` empty bottle can exchange one full bottle
        - so we can do the following steps:
            (1) define `drink_num` to record the number of bottles drinked
            (2) use `while` loop to handle the unknown rounds
            (3) in while loop:
                - `numBottles // numExchange = k`
                - add `k*numExchange` to `drink_num`
                - `numBottles - k*numExchange + k` to get the remaining bottles after exchange
            (4) if `k` == 0, end the while loop
        """
        drink_num = 0
        while True:
            k = numBottles // numExchange
            if k == 0:
                return drink_num + numBottles
            drink_num += k*numExchange
            numBottles = numBottles - k*numExchange + k
