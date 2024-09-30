class CustomStack:

    def __init__(self, maxSize: int):
        """
        thought:
        - our goal is to initialize a stack with up to `maxSize` elements.
        - therefore, we can initialize two variables:
            (1) an empty list to represent the stack.
            (2) an integer `maxSize` to set the stack's maximum capacity.
        """
        self.stack = []
        self.size = maxSize
    def push(self, x: int) -> None:
        """
        thought:
        - if the stack has not reached its `maxSize`, we should add element `x` to the top, which corresponds to the end of the list.
        - therefore, if the length of the list is less than `maxSize`, meaning we can still add elements, we should append `x` to the list.
        """
        if len(self.stack) < self.size:
            self.stack.append(x)
    def pop(self) -> int:
        """
        thought:
        - our goal is to pop and return the top element of the stack or return `-1` if the stack is empty.
        - therefore, we can follow these steps:
            - if the stack's length is zero, no elements can be popped, so return `-1`.
            - otherwise, since the stack follows a LIFO structure, we can use `list.pop()` to remove and return the top element.
        """
        if len(self.stack) == 0:
            return -1
        else:
            return self.stack.pop()
    def increment(self, k: int, val: int) -> None:
        """
        thought:
        - our goal is to increment the bottom `k` elements of the stack by `val`. If there are fewer than `k` elements in the stack, increment all the elements.
        - for example, if `stack = [1, 2, 3]`, `k = 2`, and `val = 10`, the updated stack should be `[11, 12, 3]`.
        - note that the bottom of the stack corresponds to the front of the list due to the LIFO structure.
        - therefore, we can follow these steps:
            (1) if `k` is greater than the length of the stack, set `k` to the stack's length so that all elements are incremented. Otherwise, keep `k` unchanged.
            (2) increment the value of the first `k` elements in the stack (the list) by `val`.
        """
        if k > len(self.stack):
            k = len(self.stack)
        for i in range(k):
            self.stack[i] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
