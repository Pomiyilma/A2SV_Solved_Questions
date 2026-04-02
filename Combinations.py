class Solution:
    def combine(self, n: int, k: int):
        res = []
        curr = []

        def backtrack(start):
            #base Case!
            if len(curr) == k:
                res.append(curr[:])                
                return                                              #|
                                                                    #|  goes back to this, then len(curr) = 1 again bc it's still [1]
            # pick next number                                       |  then on for loop , range (2, 5) curr.append(2) = curr = [1,2]
            for num in range(start, n + 1):  #range(1,5) in eg 1     |  then backtrack(3) means start = 3, so UPP len(curr) == 2 now ==k!
                curr.append(num)     #curr.append(1) -> curr = [1]   |  then res.append([1,2]) => res = [[1,2]]. The 2 is popped => curr = [1]
                backtrack(num + 1)#backtrack(2), means start = 2 ----|  then start = 3, then curr = [1,3] and backtrack(4), from now len == 2
                curr.pop()                                         #then for 2 and for 3...

        backtrack(1)
        return res
