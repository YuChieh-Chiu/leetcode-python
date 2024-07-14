class MyStack:

    def __init__(self):
        """
        - function: establish a `stack` using queue
        - todo: establish a list `queue` to represent a queue
        - note: queue is a FIFO data structure
        """
        self.queue = []
    def push(self, x: int) -> None:
        """
        - function: push element on the top of `stack` using queue
        - todo: append element to `queue`
        """
        self.queue.append(x)
    def pop(self) -> int:
        """
        - function: remove the element on the top of `stack` using queue
        - todo: 
            (1) since `queue` can only pop from the end, we need to continue poping from the end till length of `queue` equals to 1 
            (2) the popped out values should be stored and replace `self.queue` to represent the `stack` after popping out the last value
            (3) the last value still in `queue` is the value be popped out
        - note: `queue` is a FIFO data structure, so we need to use pop(0) to pop the first element
        """
        pop_queue = []
        while len(self.queue) > 1:
            pop_queue.append(self.queue.pop(0))
        pop_num = self.queue.pop(0)
        self.queue = pop_queue
        return pop_num
    def top(self) -> int:
        """
        - function: return the element on the top of the stack using queue
        - todo:
            (1) since `queue` can only pop from the end, we need to continue poping from the end till length of `queue` equals to 0
            (2) the popped out values should be stored and replace `self.queue` to represent the `stack` after using `top`
            (3) when length of `queue` equals to 1, get the value and return it later
        - note: `queue` is a FIFO data structure, so we need to use pop(0) to pop the first element
        """
        top_queue = []
        while len(self.queue) > 1:
            top_queue.append(self.queue.pop(0))
        top_num = self.queue.pop(0)
        top_queue.append(top_num)
        self.queue = top_queue
        return top_num
    def empty(self) -> bool:
        """
        function: check if the `stack` is empty using queue
        todo: use `length of `queue` equals to 0 or not` to check
        """
        if len(self.queue) == 0:
            return True
        else:
            return False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
