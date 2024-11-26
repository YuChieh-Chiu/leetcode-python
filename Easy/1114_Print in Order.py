"""
Thought:
- From the problem description, we know that:
    1. The same instance of `Foo` will be passed to three different threads.
    2. The threads must execute in a specific order: `first()` -> `second()` -> `third()`.
    3. The scheduling of threads by the operating system is unpredictable.
- Key Points:
    1. Implement atomic operations to prevent interruptions in each method:
        - In `__init__`, initialize `self.step = 'first'` to allow `first()` to proceed first.
        - In `first()`, update `self.step = 'second'` to allow `second()` to execute next.
        - In `second()`, update `self.step = 'third'` to allow `third()` to execute last.
    2. If a method is not allowed to execute, it should wait and yield control to others.
- Key Concepts:
    1. Concurrency
    2. Multi-threading
"""

class Foo:
    def __init__(self):
        self.step = "first"
    def first(self, printFirst: 'Callable[[], None]') -> None:
        while self.step != "first":
            continue
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.step = "second" 
    def second(self, printSecond: 'Callable[[], None]') -> None:
        while self.step != "second":
            continue
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.step = "third"
    def third(self, printThird: 'Callable[[], None]') -> None:
        while self.step != "third":
            continue
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
