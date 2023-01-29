# https://leetcode.com/problems/first-missing-positive/submissions/886947701/

class Solution:
    def firstMissingPositive(self, nums):
        nums = set(nums)
        for i in range(1, len(nums)+1):
            if i not in nums:
                return i
        else:
            return len(nums)+1