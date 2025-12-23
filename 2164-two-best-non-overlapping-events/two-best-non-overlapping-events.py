class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        INF = 10**20
        evt = []
        for s, e, v in events:
            evt.append((s, -1, v))
            evt.append((e, 1, v))
        evt.sort()
        best = -INF
        best_one_event = -INF
        for _, t, v in evt:
            if t == -1:
                best = max(best, best, best_one_event + v)
            else:
                best_one_event = max(best_one_event, v)
                best = max(best, v)
        return best