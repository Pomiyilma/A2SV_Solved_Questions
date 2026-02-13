class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        combined = [] 
        for res in responses:
            for r in set(res):
                combined.append(r)
        
        count = Counter(combined) 

        most_common = combined[0]

        for response in combined:
            if count[response] > count[most_common]:
                most_common = response
            if count[response] == count[most_common]:
                if response < most_common:
                    most_common = response
                    
        
        return most_common
