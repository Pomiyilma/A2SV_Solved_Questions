n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i, j, count = 0, 0,0
while i < len(a) and j < len(b):
  if a[i] > b[j]:
    j += 1
  elif a[i] < b[j]:
    i += 1
  else:
    count_a, count_b = 0,0
    val = a[i]
    while i < len(a) and val == a[i]:
      count_a += 1
      i += 1
    while j < len(b) and  val == b[j]:
      count_b += 1
      j += 1

    count += count_a * count_b
print(count)

  

