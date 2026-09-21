from data_structure.priority_queue import PriorityQueue


def heuersitc(param):
    # Some huerstic cost function here
    pass


def astar(start_state, target, heuersitic):
    queue = PriorityQueue()

    queue.append(start_state)

    while queue:
        cur = queue.pop(0)
        if cur == target:
            return cur, cur.cost
        queue.insert(cur.children, cost=cur.children.cost + heuersitic(cur.children.cost))

    return -1
