# https://leetcode.com/problems/maximum-gap/

class Solution:
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        nums.sort()
        return max((abs(nums[i+1]-nums[i]) for i in range(len(nums)-1)))