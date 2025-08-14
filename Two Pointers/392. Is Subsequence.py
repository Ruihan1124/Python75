# 2nd practice, easy, 2025/8/14
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        i = 0
        for j in range(len(t)):
            if i < len(s) and s[i] == t[j]:
                i += 1
        return i == len(s)
