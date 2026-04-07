from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.arr = deque([])
        self.size = size
        self.start = 0
        self.end = 0
        self.result = []

    def next(self, val: int) -> float:
        avg = None
        if len(self.arr) == self.size:
            self.arr.popleft()
            self.arr.append(val)
            avg = sum(self.arr)/self.size
            self.result.append(avg)
        elif len(self.arr) < self.size:
            self.arr.append(val)
            avg = sum(self.arr)/len(self.arr)
            self.result.append(avg)
        return avg
        
