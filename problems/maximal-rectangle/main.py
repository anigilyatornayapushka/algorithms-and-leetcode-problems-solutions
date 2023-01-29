# https://leetcode.com/problems/maximal-rectangle/

class Solution:
    def maximalRectangle(self, arr: list[list[str]]) -> int:
        max_area: int = 0
        height: int = len(arr)
        width: int = len(arr[0])
        x: int
        y: int
        k: int
        for x in range(1, width+1):
            check_area: list[str] = ['1'] * x
            for k in range(width-x+1):
                area: int = 0
                for y in range(height):
                    if arr[y][k:x+k] == check_area:
                        area += x
                    else:
                        if area > max_area:
                            max_area = area
                        area = 0
                else:
                    if area > max_area:
                        max_area = area
                    area = 0
        return max_area