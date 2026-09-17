

from typing import List, Any

class Stack():
    def __init__(self, data:List[Any]):
        super(self).__init__()
        self.data = data

    def pop(self):
        if self.data:
            return self.data.pop()

    def append(self, data):
        self.data.append(data)