def qSort(arr: list) -> list:
    if len(arr) < 2:
        return arr
    elem = arr[0]
    lt = [i for i in arr if i < elem]
    eq = [i for i in arr if i == elem]
    gt = [i for i in arr if i > elem]
    return qSort(lt) + eq + qSort(gt)
