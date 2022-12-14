"""Given the heads of two singly linked-lists headA and headB, return the node at which
the two lists intersect. If the two linked lists have no intersection at all, return null."""
"""Time comp O(N)"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def get_intersection_node(self, headA: ListNode, headB: ListNode):
        if headA is None or headB is None:
            return None

        ptr_A = headA
        ptr_B = headB

        while ptr_A != ptr_B:
            ptr_A = headB if ptr_A is None else ptr_A.next
            ptr_B = headA if ptr_B is None else ptr_B.next

        return ptr_A
    