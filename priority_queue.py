import queue

import numpy as np
from typing import Any, List


class PriorityQueue():

    def __init__(self, vals:List[Any]=None):
        self.queue = []
        if vals:
            for val in vals:
                self.insert(val)

    def insert(self, new_val):
        if not self.queue:
            self.queue.append(new_val)
        else:
            for i, val in enumerate(self.queue):
                if new_val < val:
                    self.queue.insert(i, new_val)
                    return
            self.queue.append(new_val)

    def pop(self):
        return self.queue.pop(0)

    def __str__(self):
        return f"{[val for val in self.queue]}"




PQ = PriorityQueue()
rng = np.random.default_rng(seed=42)
num = rng.integers(low=0, high=10).item() 

for i in range(10):
    PQ.insert(num)
    print(PQ)
    num =  rng.integers(low=0, high=100).item() 
    if num > 50:
        val = PQ.pop()
        print(f"{val} was popped")