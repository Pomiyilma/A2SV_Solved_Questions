import sys
input = sys.stdin.readline

test_case = int(input())
for test in range(test_case):
  n, l, r = map(int, input().split())
  colors = list(map(int, input().split()))
  left, right = {}, {}

  for i in range(l):
    color = colors[i]
    left[color] = left.get(color, 0) + 1
  for j in range(l, n):
    color = colors[i]
    right[color] = right.get(color, 0) + 1
  for c in list(left.keys()):
    if c in right:
      matched = min(left[c], right[c])
      left[c] -= matched
      right[c] -= matched
      l -= matched
      r -= matched

    cost = 0
    if l < r:
        left, right = right, left
        l, r = r, l
    diff = l - r  #balance them Using rpepeats
    moves_needed = diff // 2
    for c in left:
        while left[c] >= 2 and moves_needed > 0:
            left[c] -= 2
            moves_needed -= 1
            cost += 1
    cost += moves_needed
    #now balanceD
    remaining = r  #l == r
    cost += remaining
    
    print(cost)
