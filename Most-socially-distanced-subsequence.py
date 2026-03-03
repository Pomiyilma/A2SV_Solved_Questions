import sys
input = sys.stdin.readline

test_case = int(input())
for test in range(test_case) :
  n = int(input().strip())
  p = list(map(int, input().split()))

  res = [p[0]]

  for i in range(1, n - 1):
    if(p[i] > p[i - 1] and p[i] > p[i + 1]) or (p[i] < p[i - 1] and p[i] < p[i + 1]):
      res.append(p[i])
  res.append(p[-1])

  n = len(res)
  print(n)
  print(*res)
