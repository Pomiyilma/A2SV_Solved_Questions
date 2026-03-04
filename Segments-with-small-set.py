n, k = map(int, input().split())
a = list(map(int, input().split()))

from collections import defaultdict

freq = defaultdict(int)
left, unique, count = 0,0,0

for right in range(n):
    if freq[a[right]] == 0:#new num adding
        unique += 1
    freq[a[right]] += 1#else, add on freq(already seen)

    while unique > k:#shrinkk
        freq[a[left]] -= 1
        if freq[a[left]] == 0:
            unique -= 1 #off from unique too
        left += 1
    count += right - left + 1
print(count)
