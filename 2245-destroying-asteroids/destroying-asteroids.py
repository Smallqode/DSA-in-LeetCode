class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        N = len(asteroids)
        asteroids.sort()
        for i in range(N):
            if mass >= asteroids[i]:
                mass += asteroids[i]
            else:
                return False
        else:
            return True