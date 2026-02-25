class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        left = 0
        right = len(people) - 1
        boats = 0

        while left <= right:
            if people[left] + people[right] <= limit:    #if the heaviest can't be paired up with the lightest, 1 boat for it
                left += 1
            
            right -= 1
            boats += 1

        return boats
