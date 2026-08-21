# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        tail = temp

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1 #attach smaller node
                list1 = list1.next #move forward 
            else: 
                tail.next = list2 #attach smaller node
                list2 = list2.next #move forward 

            tail = tail.next  #move tail to the node that was just attached, next node added after 
        
        #if there is still node in the list after the loop 
        tail.next = list1 if list1 else list2 

        return temp.next
