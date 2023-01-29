def qSort(arr: list) -> list:
    return arr if len(arr) < 2 else\
        qSort(
            (lambda: [i for i in arr if i < arr[0]])()
        )\
        +\
        (lambda: [i for i in arr if i == arr[0]])()\
        +\
        qSort(
            (lambda: [i for i in arr if i > arr[0]])()
        )