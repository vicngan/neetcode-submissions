class Node: 
    def __init__(self, key= 0, value = 0):
        self.key = key
        self.value = value 
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.cache = {}

        #initialize temp node for insertion/removal 
        self.left = Node() #LRU
        self.right = Node() # MRU 

        self.left.next = self.right 
        self.right.prev = self.left 

    def remove(self, node: Node) -> None: #remove node from mid of doubly linked list 
        prev_node = node.prev
        next_node = node.next 
        #prev_node <-> node <-> next_node

        prev_node.next = next_node 
        next_node.prev = prev_node
        #prev_node <-> next_node
    
    def insert(self, node: Node) -> None:  #insert node right before the temp node 
        prev_node = self.right.prev #prev node to right before the self.right in doubly linked 
        #prev_node <-> self.right
        
        prev_node.next = node 
        node.prev = prev_node 
        #prev_node <-> node

        node.next = self.right 
        self.right.prev = node 
        #prev_node <-> node <-> self.right
        
    def get(self, key: int) -> int:
        if key not in self.cache: return -1 
        node = self.cache[key]
        
        self.remove(node)
        self.insert(node)

        return node.value 
    def put(self, key: int, value: int) -> None:
        #remove old node before replacing it 
        if key in self.cache: 
            self.remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node 
        self.insert(node)

        #if new pair causes cache to exceed capacity, remove the LRU
        if len(self.cache) > self.capacity: 
            #node immediately after self.left = LRU 
            LRU = self.left.next
            #before <-> LRU <-> after

            self.remove(LRU) #remove from linked list
            #before <-> after

            del self.cache[LRU.key] #remove from hashmap
