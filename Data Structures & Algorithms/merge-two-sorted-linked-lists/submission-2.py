# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
solving by iteration; time O(n+m) space O(1)

- to merge 2 linked lists iteratively, we loop through each step and 
keeping the ptr node at the current end of the merged list, 
and then choose the smaller head node from l1 or l2
1. create a temp node and a node ptr pointing to it 
2. if l1 and l2 not empty using while loop; check if l1 val < l2 val
3. whichever head is smaller will come next in the merged list 
4. attach that node, move ptr forward (node.next) and move list forward
5. continue until list is empty 
6. move node ptr to node.next regardless 
7. then if one list is empty
8. attach the remaining nodes from the non-empty list to the end 

'''

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1 
                list1 = list1.next
            else: 
                node.next = list2 
                list2 = list2.next
            node = node.next 
        
        if list1 is None: 
            node.next = list2 
        elif list2 is None: 
            node.next = list1 
        
        return temp.next 