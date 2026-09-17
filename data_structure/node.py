"""
Basic Node class that is used by AI Search, BFS and DFS problems.

"""

class Node():
    def __init__(self, val):
        super(self).__init__()
        self.val = val
        self.children = []

    def add_child(self, child:Node):
        self.children.append(child)

    def get_child(self):
        return self.children

    def __repr__(self):
        if self.children:
            return f"Node has a Value of {self.val} with {len(self.children)} children; {[child for child in self.children]}"
        return "Node has a Value of {self.val} with no children"