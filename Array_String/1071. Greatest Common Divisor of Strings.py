# 2nd time practice, easy, 2025/8/11
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        k = gcd(len(str1), len(str2))
        return str1[:k]

# Notes: 字符串的最大公约数”（GCD of Strings）
# 核心想法很巧： 如果存在一个字符串 x 同时整除 str1 和 str2，那么拼接顺序互换也应该得到同样的结果：str1 + str2 == str2 + str1。否则就不存在公共“因子”，答案是空串 ""。
# 一旦这个条件成立，最大公因子的长度就是 gcd(len(str1), len(str2))。取 str1 的前这么多字符.

# Notes: Greatest Common Divisor of Strings
# The core idea is clever: If there exists a string x that divides both str1 and str2, then reversing the order of concatenation should yield the same result: str1 + str2 == str2 + str1. Otherwise, there is no common factor, and the answer is the empty string "".
# Once this condition holds, the length of the greatest common divisor is gcd(len(str1), len(str2)). Take the first that many characters of str1.
