class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        N1 = len(nums1)
        N2 = len(nums2)
        INF = 10**20
        @cache
        def f(index1, index2, picked):
            if index1 == N1 or index2 == N2:
                if not picked:
                    return -INF
                return 0
            return max(
                f(index1 + 1, index2 + 1, True) + nums1[index1] * nums2[index2],
                f(index1 + 1, index2, picked),
                f(index1, index2 + 1, picked),
            )
        return f(0, 0, False)