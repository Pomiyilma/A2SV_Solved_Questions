class Solution:
    def dividePlayers(self, skill: list[int]) -> int:                #verymuch exONnb
        n = len(skill)
        skill.sort()
        total_sum = sum(skill)
        teams = n // 2
        if total_sum % teams != 0:
            return -1
        
        target = total_sum // teams
        chemistry = 0
        left = 0
        right = n - 1
        
        while left < right:
            if skill[left] + skill[right] != target:
                return -1
            chemistry += skill[left] * skill[right]
            left += 1
            right -= 1
    
        return chemistry
