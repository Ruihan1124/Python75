# 2nd time practice, easy, 2025/8/13
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        char = list(s)
        i, j = 0, len(s)-1
        while i < j:
            if char[i] not in vowels:
                i += 1
            elif char[j] not in vowels:
                j -= 1
            else:
                char[i], char[j] = char[j], char[i]
                i += 1
                j -= 1
        return "".join(char)
# Notes: 
# 1. str is immutable, need to change into list first.(list is mutable).
# 2. always forget i += 1 and j -= 1 in key operations step.
