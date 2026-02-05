class Solution:
    def findRestaurant(self, list1, list2):
        index_map = {word: i for i, word in enumerate(list1)}
        
        min_sum = float('inf')
        result = []

        for char, word in enumerate(list2):
            if word in index_map:
                index_sum = index_map[word] + char

                if index_sum < min_sum:
                    min_sum = index_sum
                    result = [word]
                elif index_sum == min_sum:
                    result.append(word)

        return result
