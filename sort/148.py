from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        dummyHead = ListNode(0)
        if not head:
            return None

        while head:
            valueToInsert = head.val
            arr.append(valueToInsert)
            head = head.next

        arr.sort()

        head = ListNode(0)
        dummyHead.next = head

        while arr:
            valueToInsert = arr.pop(0)
            head.next = ListNode(valueToInsert)
            head = head.next
        return dummyHead.next.next