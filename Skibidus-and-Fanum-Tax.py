import sys
input = sys.stdin.readline
from bisect import bisect_left

t = int(input())
for _ in range(t):
  n , m = int(input())
  a, b = list(map(int, input().split()))

  #a = [2, 4, 6, 5]  n = 4
  #b = [6, 1, 8]   m = 3

  b.sort()  # b = [1, 6, 8]
  prev = -10 ** 18
  poss = True

  for x in a:
    candidates = []
    if x >= prev:
      candidates.append(x)

    target = prev + x
    idx = bisect_left(b, target)

    if idx < m:
        transformed = b[idx] - x
        candidates.append(transformed)

    # No valid choice
    if not candidates:
        possible = False
        break

    # Greedy: choose smallest valid
    prev = min(candidates)

  print("YES" if possible else "NO")
