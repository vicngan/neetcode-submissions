class KthLargest:
#return the kth largest element (O(nlogk) time and O(k) space)

    def __init__(self, k: int, nums: List[int]):
        #minHeap, pop kth smallest interger 
        self.minHeap = nums 
        self.k = k 
        heapq.heapify(self.minHeap) #convert the list to heap 
        while len(self.minHeap) > k:  #if length is bigger than k, pop the smallest integer from the minHeap
            heapq.heappop(self.minHeap) 

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val) #add val to minHeap 
        if len(self.minHeap) > self.k:  #after adding val, if minHeap is bigger than k, pop the smallest element from heap 
            heapq.heappop(self.minHeap)

        return self.minHeap[0] #return the smallest element at the top, if heap contain k largest val, smallest = kth largest overall 
        
