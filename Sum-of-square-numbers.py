class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0    #0^2 + 5^2 = 25, a = 0 (smallest one)   let's say c = 25
        b = int(math.sqrt(c))   #b = 5 (largest one)
        
        while a <= b:
            current = a*a + b*b
            if current == c:
                return True
            elif current < c:  #if sum is too small increase a
                a += 1  
            else:
                b -= 1  #if sum is too large decrease b
        return False

        #OR but it TLEs :(
        # limit = int(math.sqrt(c))  #a and b both are < root 5 (lets say it's 2.5)        
        # for a in range(limit + 1):  
        #     for b in range(limit + 1):
        #         if a*a + b*b == c:
        #             return True
        
        # return False
