# https://leetcode.com/problems/valid-number/

class Solution:
    def isNumber(self, s: str) -> bool:
        if 'i' in s:
            return False
        try:
            int(s)
        except:
            try:
                float(s)
            except:
                return False
        return True