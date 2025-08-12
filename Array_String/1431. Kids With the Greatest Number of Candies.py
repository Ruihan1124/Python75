# 2nd time practice, easy, 2025/8/12
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        i = 0
        while i < len(candies):
            if candies[i] + extraCandies >= max(candies):
                result.append(True)
                i += 1
            else:
                result.append(False)
                i += 1
        return result

# Notes: make some silly mistakes, forget i += 1 causing exceed time limit, True and False, not true and false.
