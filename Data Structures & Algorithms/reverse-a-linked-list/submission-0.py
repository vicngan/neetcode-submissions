# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
solving with two pointers -> O(n) space and O(1) memory 

1: walk through the list from L to R, and for each node, we redirect the next ptr to the prev node 
2: initialize prev = temp and current = head 
3: run a while loop while current exist; save the next node
4: reverse the ptr by pointing from the next node -> prev node 
5: update new prev to current node
6: update current to temp 
7: when current node = null, the list is reversed and prev node point to the new curr


'''

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node, current = None, head 

        while current: 
            temp = current.next
            current.next = prev_node
            prev_node = current 
            current = temp 
        return prev_node