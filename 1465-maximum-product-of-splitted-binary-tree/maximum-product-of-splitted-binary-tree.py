# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        def get_sum(node):
            if node is None:
                return 0
            return node.val + get_sum(node.left) + get_sum(node.right)
        total = get_sum(root)
        best = -1
        def get_sum2(node):
            if node is None:
                return 0
            subsum = node.val + get_sum2(node.left) + get_sum2(node.right)
            othersum = total - subsum
            nonlocal best
            best = max(best, subsum * othersum)
            return subsum
        get_sum2(root)
        return best % MOD