class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        #we start by putting the 'biggest' one at the end. so if [3,2,4,1], k=3 brings 'biggest' in the front. then k=4, at the end
        #there is no single answer. Can be an answer as long as it sorts the array
        result = []
        n = len(arr)
        for size in range(n, 1, -1):  #from biG to small
            index = arr.index(size) #saving the index
            if index != size - 1:  #if it's not at the end
                if index != 0:    #if it's not on top
                    arr[:index + 1] = reversed(arr[:index + 1]) #flipp numbers until with iNdexes index + 1
                    result.append(index + 1)

                arr[:size] = reversed(arr[:size])
                result.append(size)
        return result
                    

