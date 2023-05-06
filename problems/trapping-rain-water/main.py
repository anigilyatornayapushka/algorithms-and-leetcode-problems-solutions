# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height):
        r = 0
        if len(height) < 3:
            return 0
        if height[0] == height[-1] == max(height):
            return height[0]*len(height)-sum(height)
        for i in range(1, len(height)-1):
            a = max(height[:i])
            b = max(height[i+1:])
            c = height[i]
            if a > c and b > c:
                r += min(a, b) - c
        return r
