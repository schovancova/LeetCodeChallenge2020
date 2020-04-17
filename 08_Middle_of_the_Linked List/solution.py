# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def get_total_count(self, head: ListNode) -> int:
        total_count = 1
        while head.next:
            total_count += 1
            head = head.next
        return total_count

    def middleNode(self, head: ListNode) -> ListNode:
        total_count = self.get_total_count(head)
        middle_idx = int(total_count / 2)
        while middle_idx > 0:
            head = head.next
            middle_idx -= 1
        return head

