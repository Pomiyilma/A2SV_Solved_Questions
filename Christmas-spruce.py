def solve():
  n = int(input())
  kids = [0] * (n + 1) #  [0,0,0,0, 0, 0, 0,0]
  parent = [0] * (n + 1)   #  [0,0,0,0, 0, 0, 0,0]

  for i in range (2, n):  #2,3,4,5,6,7
    x = int(input())
    kids[x]  += 1
    parent[i] =x 

  lc = [0] * n

  for i in range(2, n + 1):
    if kids[i] == 0:
      lc[parent[i]] += 1

  for i in range (1, n + 1):
    if lc[i] != 0 and lc[i] < 3:
      return False
