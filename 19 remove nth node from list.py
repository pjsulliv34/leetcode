# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        temp = head
        while temp:
            length +=1
            temp = temp.next
        print(length)
        temp2 = head
        prev = None
        while temp2:
            if length == n:
                if not prev:
                    return head.next
                else:
                    prev.next = temp2.next
            length -=1
            prev = temp2
            temp2 = temp2.next
        return head