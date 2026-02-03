class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        N = len(nums)

        def increasing(arr):
            N = len(arr)
            for i in range(1, N):
                if arr[i - 1] >= arr[i]:
                    return False
            return True

        def decreasing(arr):
            N = len(arr)
            for i in range(1, N):
                if arr[i - 1] <= arr[i]:
                    return False
            return True

        for p in range(1, N):
            if increasing(nums[:p+1]):
                for q in range(p+1, N-1):
                    if decreasing(nums[p:q+1]) and increasing(nums[q:]):
                        return True
        return False