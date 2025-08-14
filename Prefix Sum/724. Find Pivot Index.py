# 2nd practice, easy, 2025/8/14
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_nums = sum(nums)
        left_nums = 0
        for i in range(len(nums)):
            if left_nums == (total_nums - left_nums - nums[i]):
                return i
            left_nums += nums[i]
        return -1
