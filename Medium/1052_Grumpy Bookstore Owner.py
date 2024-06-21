class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        """
        thought:
        - the target is to maximize the number of customers that can be satisfied
            - we know the `customer` is satisfied or not only depends on the owner is `grumpy` or not, which means we should check customer and grumpy by zip()
        - the only other thing we should consider is `minutes` which can extend keep owner not grumpy and then keep customers satisfied in those times
            - so we should slide window with size = `minutes` to get the maximum number of customers which may not satisfied
        """
        tot = 0
        minutes -= 1
        for c, g in zip(customers, grumpy):
            if g == 0:
                tot += c
        # the originla window
        max_customers_not_satisfied = customers_not_satisfied = sum([customers[j]*grumpy[j] for j in range(0, minutes+1)])
        for i in range(1, len(customers)-minutes):
            # sliding window : add another element and delete the first element
            customers_not_satisfied += (customers[i+minutes]*grumpy[i+minutes] - customers[i-1]*grumpy[i-1])
            if customers_not_satisfied > max_customers_not_satisfied:
                max_customers_not_satisfied = customers_not_satisfied
        tot += max_customers_not_satisfied
        return tot
