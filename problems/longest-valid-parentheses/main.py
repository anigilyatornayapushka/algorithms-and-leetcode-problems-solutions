# https://leetcode.com/problems/longest-valid-parentheses/submissions/1009540029/

import re


class Solution:
    def longestValidParentheses(self, string: str):
        if vals := (re.findall(r'\((?:i\d+i)*\)', string) or re.findall(r'(?:i\d+i){2,}', string)):
            for n in vals:
                if n not in string:
                    continue
                N = 0
                number = ''
                for str_n in n:
                    if str_n.isdigit():
                        number += str_n
                    elif str_n in '()':
                        N += 1
                    elif number:
                        N += int(number)
                        number = ''

                N = 'i%di' % N
                while n in string:
                    string = string.replace(n, N)
        else:
            vals = [int(i) for i in re.findall(r'\d+', string)]
            if vals:
                return max(vals)
            return 0

        return self.longestValidParentheses(string)
