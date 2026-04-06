class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obs = set()
        for x, y in obstacles:
            obs.add((x, y))
        directions = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        ]
        current_direction = 0
        farthest = 0
        x = y = 0
        for command in commands:
            if command == -2:
                current_direction = (current_direction + 4 - 1) % 4
            elif command == -1:
                current_direction = (current_direction + 1) % 4
            else:
                dx, dy = directions[current_direction]                
                for _ in range(command):
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in obs:
                        break
                    x, y = nx, ny
                    farthest = max(farthest, x * x + y * y)
        return farthest