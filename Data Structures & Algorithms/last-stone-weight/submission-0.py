import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-weight for weight in stones] #store negative weight to simulate maxHeap
        heapq.heapify(stones)

        while len(stones) > 1:  #pop out 2 stones so the parameters has to be bigger than 2
            heaviest_stone = -heapq.heappop(stones)
            second_heaviest = -heapq.heappop(stones)

            if heaviest_stone != second_heaviest: 
                difference = heaviest_stone - second_heaviest 
                heapq.heappush(stones, -difference)


        return -stones[0] if stones else 0 



        

        