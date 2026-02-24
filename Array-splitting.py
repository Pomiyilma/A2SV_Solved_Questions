import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
total = a[-1] - a[0]
gaps = []

if k == 1:
    print(a[-1] - a[0])
    exit()
for i in range(n - 1):
    gaps.append(a[i+1] - a[i])
    
gaps.sort(reverse=True)
for i in range(k - 1):
    total -= gaps[i]

print(total)
