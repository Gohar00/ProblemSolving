"""Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
Return the linked list sorted as well."""
"""Time comp O(n)"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def delete_duplicates(self, head: ListNode):
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head
