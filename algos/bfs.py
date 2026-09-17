def bfs(root):

    queue = [root]
    search = [root]
    while (queue):
        cur = queue.pop(0)
        for child in cur.children:
            queue.append(child)
            search.append(child)


    return search
