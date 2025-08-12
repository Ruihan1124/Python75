# 2nd time practice, easy but worth thinking, 2025/8/12
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        else:
            m = len(flowerbed)
            i = 0
            while i < m:
                if flowerbed[i] == 0:
                    left_empty = (i == 0) or (flowerbed[i-1] == 0)
                    right_empty = (i == m-1) or (flowerbed[i+1] == 0)
                    if left_empty and right_empty:
                        n -= 1
                        if n <= 0:
                            return True
                        i += 2
                    else:
                        i += 1
                else:
                    i += 1
            return n<=0
# rough ideas: 
# 从头开始遍历，如果位置本身为0，且左右都为0，可以种，n-1,右移2个。
# 如果位置本身不为0，或者左右不同时为0，不可以种，只可以右移1个。
# 从i = 0遍历到i = m-1,最后判断n和0的关系
# Start from the beginning. If the position itself is 0, and both the left and right are 0, plant, n-1 and shift right by 2.
# If the position itself is not 0, or the left and right are not both 0, do not plant, and only shift right by 1.
# Traverse from i = 0 to i = m-1, and finally determine the relationship between n and 0.


# 1st time practice, use a easier method, 2024/9/9
# P.S. it's faster, but i fogot the idea myself when i practice again.
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        ans = 0 
        prev = -2 
        for i in range(len(flowerbed)): 
            if flowerbed[i] == 1: 
                ans = ans + max(0,(i - prev -2) // 2) 
                prev = i 
        ans = ans + max(0,(len(flowerbed) - prev -1) // 2) 
        return ans >= n
# rough ideas:
# 统计每个空地段的最大种花数 → 累加 → 判断是否够 n
# ans：统计一共能种多少花.
# prev：记录上一个已有花的位置.
# 遇到 1（已有花）的时候:计算两次之间的间隔：i - prev - 1 → 间隔长度，
# 但是需要多空出1个再除2.例如：3个空格，3-1//2 = 1，只能种1朵，2个空格，2-1//2 = 0，一朵都不能种
# [(i - prev - 1) - 1 ]//2, ans = ans + (i - prev - 2)//2
# ans初始值为0，这个很好理解，但是prev初始值应该是多少？如果i=0时，就已经有一朵了。
# 初始值也要符合通用公式: 0 - prev - 2 // 2 = 0, prev = -2，反向推导出prev = -2
# 如果i=0没有一朵花，i = 1是第一朵：1-(-2)-2//2=0, i=2是第一朵:2-(-2)-2//2=1,符合
# 再考虑最后结尾，从末尾到最后一个1，例如.....1 0 0 0后面还可以再种一个
# 这个时候间距是：[len(flowerbed)-1] - i//2, len(flowerbed)-1就是最后一个的序号了，减去i，实际是最后一段全是0的间距，这里就直接//2就可以了
# 即：考虑前面的全部，和最后一部分特殊的地方
# Count the maximum number of flowers that can be planted in each empty segment → sum them up → check if the total is at least n.
# ans: total number of flowers that can be planted.
# prev: the index of the last position that already has a flower.
# When encountering a 1 (existing flower):
# Calculate the gap between this flower and the previous one: i - prev - 1 → this is the number of empty spots.
# You need to leave one spot empty for adjacency rules, then divide by 2 to get the max flowers that can be planted in that gap.
# Example: 3 empty spots → (3 - 1) // 2 = 1 (can plant 1 flower)
# 2 empty spots → (2 - 1) // 2 = 0 (can’t plant any).
# Formula: [(i - prev - 1) - 1] // 2 → simplified to (i - prev - 2) // 2.
# Accumulate: ans += (i - prev - 2) // 2.
# ans starts at 0 (obvious), but what about prev?
# It must work with the general formula even if the first flower is at position i = 0.
# For i = 0 with a flower: (0 - prev - 2) // 2 = 0 → gives prev = -2.
# This value also works for other cases:
# If first flower at i = 1: (1 - (-2) - 2) // 2 = 0
# If first flower at i = 2: (2 - (-2) - 2) // 2 = 1.
# Then handle the last segment after the final flower:
# From the last 1 to the end of the array, e.g., ... 1 0 0 0 → you can still plant in the trailing empty spots.
# The gap length is (len(flowerbed) - 1) - i, where i is the index of the last flower.
# This gap can directly be divided by 2: (len(flowerbed) - last_flower_index - 1) // 2.
# So overall: Count all middle segments using the formula. Add the last trailing segment separately.
