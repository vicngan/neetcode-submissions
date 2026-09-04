class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for x, y in points: #calculate x, y and append to minHeap and turn that into a heap 
            distance = (x**2) + (y**2)
            minHeap.append([distance, x, y])
        heapq.heapify(minHeap)

        res = []
        while k > 0: #iterate k times 
            distance, x, y = heapq.heappop(minHeap) #pop the top value correspond to distance and cordinates
            res.append([x,y]) #append cordinates to res and move down the stack 
            k -= 1 
        return res #res of k closest points 

