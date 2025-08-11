# 2nd time practice, easy, 2025/8/11
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i, j = 0, 0
        res = []

        while i < len(word1) or j < len(word2):
            if i < len(word1):
                res.append(word1[i])
                i += 1
            if j < len(word2):
                res.append(word2[j])
                j += 1
        return ''.join(res)

# Notes: 
# 1. why 2 array?
# Because need to traverse two strings at the same time and take characters alternately in order, one pointer i is responsible for word1 and the other pointer j is responsible for word2.
# 因为要同时遍历两个字符串，并且按顺序交替取字符,一个指针 i 负责 word1，另一个指针 j 负责 word2.

# 2. "".join(res) joins all elements in the list res into a single string with "" (empty string) as the separator.
