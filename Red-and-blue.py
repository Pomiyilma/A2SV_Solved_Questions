import sys
input = sys.stdin.readline
 
t = int(input())
 
for _ in range(t):
    n = int(input())
    r = list(map(int, input().split()))
 
    m = int(input())
    b = list(map(int, input().split()))
 
    curr, best_red = 0,0
    for i in r:
        curr += i
        best_red = max(best_red, curr)
    curr, best_blue = 0, 0
    for i in b:
        curr += i
        best_blue = max(best_blue, curr)
 
    print(best_red + best_blue)
