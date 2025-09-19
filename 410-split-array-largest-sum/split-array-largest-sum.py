class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(mid):
            subarray = 0
            cur_sum = 0
            for n in nums:
                cur_sum += n
                if cur_sum > mid:
                    subarray += 1
                    cur_sum = n
            return subarray + 1 <= k

        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            mid = (l + r) // 2
            if can_split(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res