# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        adj_list = defaultdict(list)
        indegree = Counter()
        for p, c, l in descriptions:
            adj_list[p].append((c, l))
            indegree[c] += 1
        root = None
        for k in adj_list.keys():
            if indegree[k] == 0:
                root = k
                break
        assert(root is not None)
        def traverse(node):
            current = TreeNode(node)
            for c, l in adj_list[node]:
                if l:
                    current.left = traverse(c)
                else:
                    current.right = traverse(c)
            return current
        return traverse(root)