"""
Thought:
- Problem Description:
    - The same instance of `FooBar` will be passed to two different threads.
    - The functions `foo` and `bar` will be executed in separate threads.
    - The goal is to output 'foobar' `n` times.
- Key Process:
    - Define two locks, `lock1` and `lock2`, to coordinate thread execution:
        - In the first iteration, only `lock1` is considered:
            1. If `lock1` is acquired, execute the `foo` function and then release `lock1`.
            2. If `lock1` is released, execute the `bar` function and release `lock2`.
        - From the second iteration onwards, both locks are involved:
            1. If `lock2` is released and `lock1` is acquired, execute the `foo` function.
            2. If `lock1` is released, execute the `bar` function and release `lock2`.
- Key Concepts:
    - Concurrency
    - Multi-threading
    - The `Lock` module in the `threading` library
"""

from threading import Lock

class FooBar:
    def __init__(self, n):
        self.n = n
        self.lock1 = [Lock() for i in range(n)]
        self.lock2 = [Lock() for i in range(n-1)]
        for i in range(n):
            self.lock1[i].acquire()
        for i in range(n-1):
            self.lock2[i].acquire()
    def foo(self, printFoo: 'Callable[[], None]') -> None: 
        for i in range(self.n):
            if i == 0:
                # printFoo() outputs "foo". Do not change or remove this line.
                printFoo()
                self.lock1[i].release()
            else:
                with self.lock2[i-1]:
                    # printFoo() outputs "foo". Do not change or remove this line.
                    printFoo()
                    self.lock1[i].release()
    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            with self.lock1[i]:
                # printBar() outputs "bar". Do not change or remove this line.
                printBar()
                if i != self.n-1:
                    self.lock2[i].release()
