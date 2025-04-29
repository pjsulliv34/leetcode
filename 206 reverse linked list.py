# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode{{val: {self.val}, next: {repr(self.next)}}}"


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        prev = None
        curr = head
        while curr:
            temp = curr.next # temp for moving to next current node
            curr.next = prev # assigned next of current node to prev
            prev = curr # move previous pointer to current node
            curr = temp # move current node to next previous node

        return prev