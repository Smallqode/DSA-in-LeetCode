class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def check_sorted(arr):
            N = len(arr)
            for i in range(N - 1):
                if arr[i] > arr[i + 1]:
                    return False
            return True
        def do_operation(arr):
            N = len(arr)
            best_index = 0
            for i in range(1, N - 1):
                if arr[i] + arr[i + 1] < arr[best_index] + arr[best_index + 1]:
                    best_index = i
            arr = arr[:best_index] + [arr[best_index] + arr[best_index + 1]] + arr[best_index + 2:]
            return arr
        operations = 0
        while not check_sorted(nums):
            nums = do_operation(nums)
            operations += 1
        return operations