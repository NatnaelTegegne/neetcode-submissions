# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        pointer = head
        seen = set()

        while(pointer.next):
            if(pointer.val in seen):
                return True
            seen.add(pointer.val)
            pointer = pointer.next
        

        return False

