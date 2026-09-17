from typing import List, Any


class Queue():
    def __init__(self,data: List[Any]):
        super(self).__init__()
        self.data = data

    def pop(self) -> Any:
        if self.data:
            return self.pop(0)

    def append(self, data:Any) -> None:
        self.append(data)

