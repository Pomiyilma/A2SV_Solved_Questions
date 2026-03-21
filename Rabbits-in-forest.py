class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        seen = defaultdict(int)
        total = 0

        for x in answers:
            g = x + 1
            if seen[g] % g == 0:
                total += g
            seen[g] += 1

        return total
