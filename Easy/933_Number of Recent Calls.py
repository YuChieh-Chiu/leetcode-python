class RecentCounter:
    """
    thought:
    - we know that
        (1) `RecentCounter()` initializes the counter with zero recent requests
        (2) `ping(t)` counts requests number in closed interval [t-3000, t]
        (3) each test case will call ping with strictly increasing values of t
    - so we get the information that [t-3000, t] is a `sliding window` from left to right (2&3)
    - and then we know RULE of the SLIDING WINDOW is as below
        (1) every time we `ping(t)`, the value of `t` should append into the end of the window
        (2) every time we `ping(t)`, we should go through window from the left border to check which value should be popped out of the window (the window size is [t-3000, t] & the ping call is strictly increasing)
    - follow the RULE mentioned above, we should use `QUEUE` to store the requests (FIFO)
    """
    def __init__(self):
        self.requests = []
    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[0] < (t-3000):
            self.requests.pop(0)
        return len(self.requests)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
