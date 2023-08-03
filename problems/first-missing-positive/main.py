# https://leetcode.com/problems/first-missing-positive/

class Solution:
    def firstMissingPositive(self, nums):
        nums = set(nums)
        for i in range(1, len(nums)+1):
            if i not in nums:
                return i
        else:
            return len(nums)+1
