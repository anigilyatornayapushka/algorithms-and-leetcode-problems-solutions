import typing as t


def find_max_sum_subarray(arr: t.Iterable[int]) -> int:
    max_s = 0
    s = 0
    for val in arr:
        s     = max(s+val, 0)
        max_s = max(max_s, s)
    return max_s
