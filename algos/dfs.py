def df(root):

    stack = [root]
    search = [root]
    while (stack):
        cur = stack.pop()
        for child in cur.children:
            stack.append(child)
            search.append(child)


    return search
