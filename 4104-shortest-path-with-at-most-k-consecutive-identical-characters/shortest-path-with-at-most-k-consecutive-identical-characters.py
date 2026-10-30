class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        INF = 10 ** 20
        adj_list = defaultdict(list)
        for u, v, w in edges:
            adj_list[u].append((v, w))
        best = defaultdict(lambda: INF)
        def enqueue(node, distance, cons):
            heappush(h, (distance, cons, node))
            best[(node, cons)] = distance
        h = []
        enqueue(0, 0, 1)
        while len(h) > 0:
            d, c, current = heappop(h)
            if current == n - 1:
                return d
            if best[(current, c)] < d:
                continue
            for v, w in adj_list[current]:
                nd = d + w
                nc = 1
                if labels[current] == labels[v]:
                    nc = c + 1
                if nc <= k and nd < best[(v, nc)]:
                    enqueue(v, nd, nc)
        return -1