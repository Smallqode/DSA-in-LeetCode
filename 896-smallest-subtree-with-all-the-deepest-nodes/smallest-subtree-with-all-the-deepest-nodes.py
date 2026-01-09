# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        deepest = -1
        count = 0
        def traverse(node, level):
            if node is None:
                return
            nonlocal deepest
            nonlocal count
            if level > deepest:
                deepest = level
                count = 1
            elif level == deepest:
                count += 1
            traverse(node.left, level + 1)
            traverse(node.right, level + 1)
        traverse(root, 0)
        ret = None
        def traverse2(node, level):
            if node is None:
                return 0
            c = 0
            if level == deepest:
                c += 1
            l = traverse2(node.left, level + 1)
            r = traverse2(node.right, level + 1)
            c += l + r
            if c == count:
                nonlocal ret
                if ret is None:
                    ret = node
            return c
        traverse2(root, 0)
        return ret