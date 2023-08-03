import typing as t


class Permutator:

    def as_generator(self, data: t.Iterable, /, __result: str = ''):
        if not data:
            yield __result

        for i in range(len(data)):
            other: t.Iterable = data[:i] + data[i+1:]

            word: str
            for word in self.as_generator(other, __result+data[i]):
                yield word

    def as_iterator(self, data: t.Iterable):
        if len(data) == 1:
            return data

        all_: list = []
        for i in range(len(data)):
            other = data[:i] + data[i+1:]

            for w in self.as_generator(other):
                all_.append(data[i] + w)
        return all_
