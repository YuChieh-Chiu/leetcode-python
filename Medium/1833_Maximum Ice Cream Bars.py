from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        """
        Thought:
        - Goal: Maximize the number of ice cream bars that can be bought with `coins`, strictly using the counting sort algorithm.
        - Idea: Instead of a full comparison-based sort, we can tally the occurrences of each cost using an array (since costs are bounded). We only care about ice creams we can afford, so we cap the counting array size at `coins`. Then, we greedily buy from the cheapest price up to the maximum we can afford.
        - Steps:
            1. Initialize a `price_count` array of size `min(max(costs), coins) + 1` with zeros.
            2. Iterate through `costs` and increment the count for each cost, ignoring any cost strictly greater than `coins`.
            3. Iterate through the `price_count` array using `price` and `count`.
            4. Skip prices that have a `count` of 0.
            5. If the remaining `coins` cannot buy all ice creams at the current `price`, buy as many as possible (`coins // price`), add to `total`, and break the loop.
            6. Otherwise, buy all `count` ice creams at this `price`, deduct the total cost from `coins`, and add `count` to `total`.
        - Time Complexity: O(N + M), where N is the length of `costs` and M is the value of `coins`. We iterate through the costs array once and the frequency array once.
        - Space Complexity: O(M), where M is the value of `coins`, due to the size of the `price_count` array.
        """
        price_count = [0] * (min(max(costs), coins) + 1)
        total = 0

        for cost in costs:
            if cost <= coins:
                price_count[cost] += 1

        for price, count in enumerate(price_count):
            if count == 0:
                continue
            
            if coins < price * count:
                total += coins // price
                break
            else:
                coins -= price * count
                total += count

        return total
