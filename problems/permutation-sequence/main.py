# https://leetcode.com/problems/permutation-sequence/

class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        def permut(data, __result):
            if not data:
                yield __result
            for i in range(len(data)):
                other = data[:i] + data[i+1:]
                for word in permut(other, __result+data[i]):
                    yield word

        nums = [str(i) for i in range(1, n+1)]
        i = 1
        for n in permut(nums, ''):
            if i == k:
                break
            i += 1
        return n
