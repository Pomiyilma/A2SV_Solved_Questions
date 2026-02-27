class Solution:
    def partitionLabels(self, s: str):
        last = {}  #dict

        for i, ch in enumerate(s):  #0,a  1,b  2,a  3,b  4,c..
            last[ch] = i     #it overwriTes it so it's ok (TO SAVE THE LAST OCURRENCE INDEXXXx) 
            #last['a'] = 0
            #last['b'] = 1
            #last['a'] = 2
            #last['b'] = 3...
        
        result = []
        start, end = 0, 0
        for i, ch in enumerate(s):
            end = max(end, last[ch])   #if last[a] = 8, we don cut at least until 8
            
            if i == end:  #if we reached tHe furthest point where it's ok to cut,
                result.append(end - start + 1)   #the size of this partition
                start = i + 1   #then start a new partition
        
        return result
        
