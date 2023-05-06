class Range:
    """Custom range."""

    def __init__(
            self,
            start: int,
            stop: int = 0,
            step: int = 1,
            /) -> None:
        self.start = start
        self.stop = stop
        if stop is 0:
            self.start, self.stop = self.stop, self.start
        self.step = step

    def __iter__(self) -> int:
        while self.start < self.stop:
            yield self.start
            self.start += self.step
