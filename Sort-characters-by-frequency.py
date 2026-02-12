class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)

        sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        
        output = ""
        
        for char, count in sorted_chars:
            output += char * count
        
        return output

#unfinished approach 1:
        #output = ""
        #freq = Counter(s)
        #maxim = 0
        #for char in s:
            #minim = max(minim, freq[char])
            #output.append(char) 
