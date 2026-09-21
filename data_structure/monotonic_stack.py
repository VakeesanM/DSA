from random import randint
"""
A Monotonic Stack is a Stack that pop values when you push new values to. 

There are two types:

Increasing: 

* When new values are pushed, the stack will repeadlety pop, until it finds a value less than it. 
* This type of monotic stack will always be sorted from least to greatest. 
* self.stack[-1] >= val


* Example:
** 10, 12, 39, 90. 20 is inserted. 90 is popped. 30 is poped. 12 is less than 20. The final result is 10, 12, 20.

Decreasing:
* When new values are pushed, the stack will repeadlety pop, until it finds a value greator than it. 
* This type of monotic stack will always be sorted from greatest to least. 
* self.stack[-1] <= val

* Example:
** 90, 39, 12, 10. 20 is inserted. 10 is popped, 12 is popped. Final result is 90, 39, 20.


"""




from typing import List, Any


class MonotonicStack():
    def __init__(self):
        self.stack = []

    def push(self, values: List[Any]):

        for i, val in enumerate(values):
            while self.stack and self.stack[-1] <= val: # Increasing Monontic Stack
                self.stack.pop()

            self.stack.append(val)


    def pop(self):
        return self.stack.pop()

    def __repr__(self):
        return f'{[val for val in self.stack]}'



             

stack = MonotonicStack()

for i in range(10):
    rnd = randint(0,100)
    print(f"new val: {rnd}")
    stack.push([rnd])
    print(stack)