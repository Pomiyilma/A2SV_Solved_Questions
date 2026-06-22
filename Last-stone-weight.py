class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]  #[-2,-7,-4,-1,-8,-1]
        heapq.heapify(stones)       #[-8,-7,-4,-2,-1,-1]

        while len(stones)  > 1:
            max1 = heapq.heappop(stones)  #-8
            max2 = heapq.heappop(stones)   #-7

            if max2 > max1:
                heapq.heappush(stones, max1 - max2)

        stones.append(0)
        return abs(stones[0])

        
