"""
Thought:  
- Problem Description:  
    - The same instance of `ZeroEvenOdd` will be passed to three different threads.  
    - The functions `zero`, `even`, and `odd` will run in separate threads.  
    - The goal is to output the series "01020304..." up to `n` times.  
- Key Point:  
    - Every time the `zero` function prints zero, it should be followed by printing either an odd or an even number.  
    - Proper synchronization between threads is required to ensure the correct sequence.  
- Key Process:  
    - Define three locks: `lock0`, `lock1`, and `lock2`, to coordinate thread execution.  
        - zero():  
            - In the first iteration, print zero immediately.  
            - In subsequent iterations:  
                - If it's an odd round, wait for `lock2` to be released (indicating that the even number has been printed), then print zero and signal the odd number to follow.  
                - If it's an even round, wait for `lock1` to be released (indicating that the odd number has been printed), then print zero and signal the even number to follow.  
        - odd():  
            - In odd rounds, wait for `lock0` to be released (indicating that zero has been printed), then print the odd number.  
            - Otherwise, do nothing.  
        - even():  
            - In even rounds, wait for `lock0` to be released (indicating that zero has been printed), then print the even number.  
            - Otherwise, do nothing.  
- Key Concepts:  
    - Concurrency  
    - Multi-threading  
    - Using the `Lock` module from the `threading` library  
"""

from threading import Lock

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.lock0 = [Lock() for i in range(self.n)]
        self.lock1 = [Lock() for i in range(self.n)]
        self.lock2 = [Lock() for i in range(self.n)]
        for i in range(self.n):
            self.lock0[i].acquire()
        for i in range(self.n):
            self.lock1[i].acquire()
        for i in range(self.n):
            self.lock2[i].acquire()
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            if i == 0:
                printNumber(0)
                self.lock0[i].release()
            else:
                if (i+1) % 2 == 0:
                    with self.lock1[i-1]:
                        printNumber(0)
                        self.lock0[i].release()
                else:
                    with self.lock2[i-1]:
                        printNumber(0)
                        self.lock0[i].release()
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            if (i+1) % 2 == 0:
                with self.lock0[i]:
                    printNumber(i+1)
                    self.lock2[i].release()
            else:
                pass   
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            if (i+1) % 2 != 0:
                with self.lock0[i]:
                    printNumber(i+1)
                    self.lock1[i].release()
            else:
                pass
