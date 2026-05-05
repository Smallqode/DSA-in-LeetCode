# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def get_length(head):
            current = ListNode(-1, head)
            count = 0
            while current.next is not None:
                current = current.next
                count += 1
            return count
        N = get_length(head)
        if N == 0:
            return None
        k %= N
        if k == 0:
            return head
        k = N - k
        new_head = ListNode(-1, head)
        current = new_head
        for _ in range(k):
            current = current.next
        next_node = current.next
        current.next = None
        last_node = next_node
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = new_head.next
        return next_node