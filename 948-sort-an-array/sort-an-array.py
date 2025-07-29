class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, L, M, R):
            left, right = arr[L:M+1], arr[M+1:R+1]
            i, j, k = L, 0, 0

            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1
            while j < len(left):
                nums[i] = left[j]
                j += 1
                i += 1
            while k < len(right):
                nums[i] = right[k]
                k += 1
                i += 1
        
        def merge_sort(arr, L, R):
            if L == R:
                return arr
            m = (L + R) // 2
            merge_sort(arr, L, m)
            merge_sort(arr, m + 1, R)
            merge(arr, L, m, R)
            return arr
        return merge_sort(nums, 0, len(nums) - 1)