# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None: 
        if not head or not head.next:
            return
        #floyd 
        slow, fast = head, head.next
        
        while fast is not None and fast.next is not None: 
            slow, fast = slow.next, fast.next.next

        #split list into halves 
        second = slow.next
        slow.next = None 

        #reverse second half 
        prev = None 

        while second: 
            next_node = second.next 
            second.next = prev
            prev = second 
            second = next_node 

        #merge 2 halves alternatively 
        first, second = head, prev 

        while second: 
            first_next = first.next 
            second_next = second.next 

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next