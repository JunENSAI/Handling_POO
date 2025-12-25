"""
Scenario: You are designing a sensor analytics tool. Data comes in strictly sequential order (a stream). 
You need to calculate the Moving Average of the last size elements.

Requirements:

Create a class MovingAverage.
    - __init__(self, size: int): Initialize with a window size.
    - next(self, val: int) -> float: Add a new value to the stream.
    - if the window is full, the oldest value falls off.
    - Return the average of the current window.

Strict Constraints (The Trap):
- The next() method must run in O(1) Time Complexity.
- Hint: If you use sum(my_window) inside next(), that is O(N). You failed.
"""

from collections import deque

class MovingAverage:

    def __init__(self, size : int):
        self.size = size
        self.window = deque()
        self.current_sum = 0

    def __str__(self):
        return f"Stream size: {self.size}, Stream content: {list(self.window)}"

    
    def next(self, val : int) -> float:
        self.window.append(val)
        self.current_sum += val

        if len(self.window) > self.size:
            removed = self.window.popleft()
            self.current_sum -= removed

        return self.current_sum / len(self.window)


def main():
    m = MovingAverage(3)
    m.next(1)
    m.next(10)
    m.next(3)
    m.next(5)
    print(m)

if __name__ == '__main__':
    main()
        