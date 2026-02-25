class Solution:
    def hIndex(self, citations: List[int]) -> int:

        n = len(citations)  #citations = [3,0,6,1,5] n = 5

        for h in range(n, 0, -1):   #range(5, 0, -1)   5,4,3,2,1,0
            num_papers = 0

            for c in citations:
                if c >= h:     
                    num_papers += 1  
            if num_papers >= h:  
                return h

        return 0
      
