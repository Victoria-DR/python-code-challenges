def index_all(lst, value):
    indices = []

    for i in range(len(lst)):
        if lst[i] == value:
            indices.append([i])
        elif type(lst[i]) == list:
            for index in index_all(lst[i], value):
                indices.append([i] + index)

    return indices

#print(index_all([[[1, 2, 3], 2, [1, 3]], [1, 2, 3]], 2))
