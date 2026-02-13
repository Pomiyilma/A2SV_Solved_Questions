class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        s1 = list(s1)
        s2 = list(s2)
        swaps = 0

        for i in range(len(s1)):
            if(s1[i] != s2[i]):
                for j in range(i + 1, len(s1)):
                    if(s1[i] == 'x' and s2[i] == 'y') and (s1[j] == 'x' and s2[j] == 'y'):
                        s1[i] , s2[j] = s2[j] , s1[i]
                        swaps += 1
                        break
                    if(s1[i] == 'y' and s2[i] == 'x') and (s1[j] == 'y' and s2[j] == 'x'):
                        s1[i] , s2[j] = s2[j] , s1[i]
                        swaps += 1
                        break
        remaining = []
        for i in range(len(s1)):
            if(s1[i] != s2[i]):
                remaining.append(i)
        if len(remaining) == 0:
            return swaps
        if(len(remaining)) == 2:
            swaps += 2
            return swaps
        return -1


        # for a, b in zip(s1, s2):
        #     if a == 'x' and b == 'y':
        #         count_xy += 1 
        #     elif a == 'y' and b == 'x':
        #         count_yx += 1 
        #     if(count_xy + count_yx) % 2 != 0:
        #         return -1
        #     total_swaps = (count_xy // 2) + (count_yx // 2)
        #     if (count_xy % 2 == 1):
        #         total_swaps += 2
