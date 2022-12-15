"""Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head."""
"""Time comp O(n^2)"""

class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertion_sort_list(self, head: ListNode):
        dummy = ListNode(0)
        cur = head

        while cur:
            prev = dummy
            while prev.next and prev.next.val < cur.val:
                prev = prev.next
            nxt = cur.next
            cur.next = prev.next
            prev.next = cur
            cur = nxt
        return dummy.next
