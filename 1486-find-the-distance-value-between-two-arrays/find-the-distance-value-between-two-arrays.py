class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        def found(x):
            for y in arr2:
                if abs(x - y) <= d:
                    return True
            return False
        count = 0
        for x in arr1:
            if not found(x):
                count += 1
        return count