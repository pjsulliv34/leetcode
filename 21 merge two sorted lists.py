# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        result = dummy # set to result, allows you to return result after moving pointer through list

        while list1 and list2:
            val1 = list1.val
            val2 = list2.val

            # no need to create new nodes, just point to the original lists
            if val1 <= val2:
                result.next = list1 # set pointer to current list1 node
                list1 = list1.next # move list1 pointer
            else:
                result.next = list2
                list2 = list2.next 
            result = result.next # moving result pointer


        # Check for stragllers

        if list1:
            result.next = list1
        if list2:
            result.next = list2


        return dummy.next
            

           