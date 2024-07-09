class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        """
        thought:
        - Note that the arrival times are sorted in non-decreasing order, meaning the order of food preparation follows the order in the list `customers`.
        - Therefore, we can follow these steps:
        1. Initialize two variables: `total` to record the total waiting time and `chef_start` to record the time the chef starts preparing food for customer `i`. Set both variables to 0.
        2. For each customer `i`, perform the following:
            a. Update the time when the chef starts preparing food for customer `i`: 
                - If `chef_start` is less than the arrival time of customer `i`, the chef can start preparing food as soon as the customer arrives.
                - Otherwise, it means the chef is still preparing food for the previous customer, so customer `i` must wait until the chef finishes.
            b. Calculate the waiting time for customer `i` by subtracting the arrival time of customer `i` from `chef_start` and then adding the food preparation time for customer `i`.
            c. Add the calculated time from step _b._ to `total`.
            d. Update `chef_start` for the next customer by adding the preparation time for customer `i` to the current `chef_start`.
        3. Divide `total` by the number of customers (`len(customers)`) to get the average waiting time.
        """
        total = chef_start = 0
        for customer in customers:
            chef_start = max(chef_start, customer[0]) # (2)-a.
            total += chef_start - customer[0] + customer[1] # (2)-b. & (2)-c.
            chef_start += customer[1] # (2)-d.
        return total/len(customers)
