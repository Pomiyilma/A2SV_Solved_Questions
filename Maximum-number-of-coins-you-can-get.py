class Solution:
    def maxCoins(self, piles: List[int]) -> int:        #exONnb
        piles.sort()           #o(nlogn) time
        i, j = 0, len(piles) - 1
        total = 0          #to keep track of what I get
        while i < j:
            total += piles[j - 1]
            i += 1
            j -= 2
        return total

     #eg: piles = [2,4,1,2,7,8]:  piles.sort() = [1,2,2,4,7,8]  j = 5
                                          #       ^       ^ ^
                                           #     i=0     j-1 j   .... total = 0+7=7
                                           #     i=1     j=3   .... total = 7+2=9
                                           #     i=2     j=1   .... total = 7+2=9

