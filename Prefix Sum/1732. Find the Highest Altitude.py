# 2nd practice, easy, 2025/8/14
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_altitude = 0
        max_altitude = current_altitude
        for i in range(len(gain)):
            current_altitude += gain[i]
            max_altitude = max(current_altitude,max_altitude)
        return max_altitude
