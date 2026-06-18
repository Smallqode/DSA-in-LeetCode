class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hdegree = float(hour) * 30 + (float(minutes)/60) * 30
        mdegree = float(minutes * 6)
        angle = abs(hdegree - mdegree)
        return min(angle, 360 - angle)