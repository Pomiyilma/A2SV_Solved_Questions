import sys
input = sys.stdin.readline

t = int(input())
for test in range(t):
    s = input().strip()
    works = set()
    i = 0
    
    while i < len(s):
        j = i
        while j < len(s) and s[j] == s[i]:
            j += 1
        length = j - i
        if length % 2 == 1:
            works.add(s[i])
        i = j
    print(''.join(sorted(works))) #alpabetical
