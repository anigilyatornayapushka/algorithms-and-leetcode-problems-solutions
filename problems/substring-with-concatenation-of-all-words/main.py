# https://leetcode.com/problems/substring-with-concatenation-of-all-words/

from collections import Counter


class Solution:

    def findSubstring(self, s, words):
        word_l = len(words[0])
        words_l = len(words)
        max_l = word_l * words_l

        res = []
        for idx in range(len(s)-max_l+1):
            if s[idx:idx+word_l] in words:
                print('Find:', s[idx:idx+word_l])
                counter = Counter(words)
                for i in range(words_l):
                    a = idx+i*word_l
                    b = idx+(i+1)*word_l
                    word = s[a:b]
                    if counter[word] == 0:
                        break
                    counter[word] -= 1
                else:
                    res.append(idx)

        return res
