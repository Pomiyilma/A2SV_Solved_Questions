import sys
input = sys.stdin.readline
 
test_case = int(input())
 
for test in range(test_case):
    n, k = map(int, input().split())
    s = input().strip()
 
    white = s[:k].count('W') #whites in first window
    ans = white
 
    for i in range(k, n):
        if s[i - k] == 'W': #slide
            white -= 1
        if s[i] == 'W':
            white += 1
        ans = min(ans, white)
    print(ans)
