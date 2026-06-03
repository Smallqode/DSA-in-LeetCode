class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        INF = 10 ** 20

        def f(landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]):
            best = INF
            landEnds = INF
            for s, d in zip(landStartTime, landDuration):
                landEnds = min(landEnds, s + d)
            for s, d in zip(waterStartTime, waterDuration):
                if s >= landEnds:
                    best = min(best, s + d)
                else:
                    best = min(best, landEnds + d)
            return best
        return min(f(landStartTime, landDuration, waterStartTime, waterDuration), f(waterStartTime, waterDuration, landStartTime, landDuration))