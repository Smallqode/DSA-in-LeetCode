class Solution:
    def countMentions(self, N: int, events: List[List[str]]) -> List[int]:
        offline = [-1000] * N
        ans = [0] * N
        f = {
            'MESSAGE': 1,
            'OFFLINE': 0
        }
        events.sort(key=lambda x: (int(x[1]), f[x[0]]))
        for t, ts, p in events:
            ts = int(ts)
            if t == 'MESSAGE':
                ms = p

                if ms == 'HERE':
                    for uid in range(N):
                        if offline[uid] <= ts:
                            ans[uid] += 1
                elif ms == 'ALL':
                    for uid in range(N):
                        ans[uid] += 1
                else:
                    uids = map(int, list(x[2:] for x in ms.split(" ")))
                    for uid in uids:
                        ans[uid] += 1
            else:
                uid = int(p)
                offline[uid] = ts + 60
        return ans