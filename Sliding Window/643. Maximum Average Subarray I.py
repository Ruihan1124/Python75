# 2nd practice, easy, 2025/8/14
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[:k])
        max_sum = current_sum
        for i in range(k,len(nums)):
            current_sum += nums[i] - nums[i-k]
            max_sum = max(current_sum,max_sum)
        return round(max_sum/k,5)
