class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for x, y in points: #calculate x, y and append to minHeap and turn that into a heap 
            distance = -((x**2) + (y**2))
            heapq.heappush(maxHeap, [distance, x, y])
            if len(maxHeap) > k: heapq.heappop(maxHeap)

        res = []
        while maxHeap: #iterate k times 
            distance, x, y = heapq.heappop(maxHeap) #pop the top value correspond to distance and cordinates
            res.append([x,y]) #append cordinates to res 
        return res #res of k closest points 

