# Implementation of the Levenshtein search algorithm

class Levenstein:

    memoize = {}

    def find(self, str1: str, str2: str) -> int:
        if result := self.memoize.get((str1, str2)):
            return result

        n = len(str1)
        m = len(str2)

        curr_l = range(n+1)

        for i in range(1, m+1):

            prev_l, curr_l = curr_l, [i] + [0]*n

            for j in range(1, n+1):

                a = prev_l[j] + 1
                b = curr_l[j-1] + 1
                c = prev_l[j-1] + (str1[j-1] != str2[i-1])
                curr_l[j] = min(a, b, c)

        result = self.memoize[(str1, str2)] = curr_l[n]
        return result

    def matrix_find(self, str1: str, str2: str) -> int:
        if result := self.memoize.get((str1, str2)):
            return result

        n = len(str1)
        m = len(str2)

        matrix = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if not i:
                    matrix[i][j] = j
                elif not j:
                    matrix[i][j] = i
                else:
                    a = matrix[i-1][j] + 1
                    b = matrix[i][j-1] + 1
                    c = matrix[i-1][j-1] + (str1[j-1] != str2[i-1])
                    matrix[i][j] = self.memoize[(str1[:i], str2[:j])] = min(a, b, c)

        return matrix[-1][-1]
