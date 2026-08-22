"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #use a hash map to map each new node with it's original node
        old_new = {None:None}

        #create a copy of every node 
        curr = head 
        while curr: 
            old_new[curr] = Node(curr.val)
            curr = curr.next 

        #connect next and random ptr 
        curr = head #original
        while curr:
            copied = old_new[curr] #new node/ copied version of the current node 
            copied.next = old_new[curr.next] #connect 
            copied.random = old_new[curr.random] #random points to any node in the list or none (arbitrary connection of a node)

            curr = curr.next 
        
        return old_new[head]