def custom_range(start: int, end: int = None, step: int = None, /) -> list[int]:
    data: list = []
    if end is None and step is None:
        if not isinstance(start, int):
            raise TypeError

        val = 0
        while val < start:
            data.append(val)
            val += 1
        del val

    elif step is None:
        if not isinstance(start, int) or not isinstance(end, int):
            raise TypeError

        val = start
        while val < end:
            data.append(val)
            val += 1
        del val

    else:
        if not isinstance(start, int) or not isinstance(end, int) or not isinstance(step, int):
            raise TypeError

        val = start
        if step == 0 or step < 0 and start < end or step > 0 and start > end:
            return []
        while start <= val < end:
            data.append(val)
            val += step
        del val

    return data