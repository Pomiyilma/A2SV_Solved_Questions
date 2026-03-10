class Solution:
    def shiftingLetters(self, s, shifts):
        n = len(s)
        diff = [0] * (n + 1)
        for start, end, direction in shifts:
            if direction == 1:
                diff[start] += 1
                diff[end + 1] -= 1
            else:
                diff[start] -= 1
                diff[end + 1] += 1
        shift = 0
        res = []
        for i in range(n):
            shift += diff[i]
            num = ord(s[i]) - ord('a')
            num = (num + shift) % 26
            res.append(chr(num + ord('a')))

        return "".join(res)
