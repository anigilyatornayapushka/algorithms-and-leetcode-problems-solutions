# https://leetcode.com/problems/max-points-on-a-line/

class Solution:
    def maxPoints(self, points):
        max_a = 0
        if len(points) < 3:
            return len(points)
        for i in points:
            all_lines = {
                'v' : 1,
                'h' : 1,
            }
            for j in points:
                if i == j:
                    continue
                coord = (j[0]-i[0], j[1]-i[1])
                if coord[0] == 0:
                    all_lines['v'] += 1
                elif coord[1] == 0 :
                    all_lines['h'] += 1
                else:
                    for k in all_lines:
                        if k != 'h' and k != 'v':
                            if k[0] / coord[0] == k[1] / coord[1]:
                                all_lines[k] += 1
                                break
                    else:
                        all_lines[coord] = 2
            maximum = 0
            for key in all_lines:
                if all_lines[key] > maximum:
                    maximum = all_lines[key]
            if maximum > max_a:
                max_a = maximum
        return max_a
