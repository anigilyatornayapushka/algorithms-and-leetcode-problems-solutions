def pigeonholes_sort(arr: list) -> list:
    pigeonholes: list = [[] for _ in range(max(arr)+1)]
    for elem in arr:
        pigeonholes[elem].append(elem)

    retern_array: list = []
    for elem in pigeonholes:
        retern_array.extend(elem)

    return retern_array
