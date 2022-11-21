func = lambda x, y: y if x == y else y + func(x, y - 1)
