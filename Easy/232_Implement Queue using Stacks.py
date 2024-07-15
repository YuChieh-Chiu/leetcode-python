class MyQueue:

    def __init__(self):
        """
        - function: establish a `queue` using stack
        - todo: 
            (1) establish a list `stack` to represent a stack
            (2) establish the other list `popout` to represent another stack
        - note: 
            (1) stack is a LIFO data structure
            (2) out target here is to implement the queue such that each operation is amortized O(1) time complexity
        """
        self.stack = []
        self.popout = []
    def push(self, x: int) -> None:
        """
        - function: push element at the end of `queue` using stack
        - todo: append element to `stack`
        """
        self.stack.append(x)
    def pop(self) -> int:
        """
        - function: remove the element from the front of `queue` using stack
        - todo: 
            (1) we use `popout` to record the elements that should be popped out from LAST to FIRST
            (2) if `popout` is empty, which means there's still no popped out elements been recorded, we should traverse `stack` and pop out the elements from last to first and append to `popout`
            (3) return the last element in `popout` use pop()
        - note: `stack` is a LIFO data structure, so we need to use pop() to pop the last element
        """
        if not self.popout:
            while self.stack:
                self.popout.append(self.stack.pop())
        return self.popout.pop()
    def peek(self) -> int:
        """
        - function: return the element at the front of the queue using stack
        - todo:
            (1) we use `popout` to record the elements that should be popped out from LAST to FIRST
            (2) if `popout` is empty, which means there's still no popped out elements been recorded, we should traverse `stack` and pop out the elements from last to first and append to `popout`
            (3) use pop() to get the last element in  `popout`, which is the first element of queue
        - note: `stack` is a LIFO data structure, so we need to use pop() to pop the last element
        """
        if not self.popout:
            while self.stack:
                self.popout.append(self.stack.pop())
        peek_ele = self.popout.pop()
        self.popout.append(peek_ele)
        return peek_ele
    def empty(self) -> bool:
        """
        function: check if the `queue` is empty using stack
        todo: use `length of `stack` & `popout` equals to 0 or not` to check
        """
        if (len(self.stack) == 0) & (len(self.popout) == 0):
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
