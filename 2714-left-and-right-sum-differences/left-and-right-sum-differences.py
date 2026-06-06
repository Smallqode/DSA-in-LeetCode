class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftSum = [0]
        rightSum = [0]
        count = 0
        for x in nums:
            leftSum.append(x + leftSum[-1])
        for x in nums[::-1]:
            rightSum.append(x + rightSum[-1])
        rightSum.reverse()

        res = []
        for i in range(n):
            res.append(abs(leftSum[i] - rightSum[i + 1]))
        return res