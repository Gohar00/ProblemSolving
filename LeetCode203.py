"""Given the head of a linked list and an integer val, remove all
the nodes of the linked list that has Node.val == val, and return the new head.
"""
"""Time comp. O(n)"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def remove_element(self, head: ListNode, val=None):
        dummy = ListNode(next=head)
        prev = dummy
        cur = head

        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return dummy.next




