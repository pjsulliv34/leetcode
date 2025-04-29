# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
       temp = head
       visited = set()
       while temp:
        # print(temp.val)
        if (temp.val, temp.next) in visited:
            return True
        visited.add((temp.val,temp.next))
        temp = temp.next