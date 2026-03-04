import sys
input = sys.stdin.readline
from collections import defaultdict
 
n, k = map(int, input().split())
a = list(map(int, input().split()))
 
freq = defaultdict(int)
left, unique, best_length, best_left, best_right = 0,0,0,0,0
 
for right in range(n):
    if freq[a[right]] == 0:
        unique += 1
    freq[a[right]] += 1
 
    while unique > k:
        freq[a[left]] -= 1
        if freq[a[left]] == 0:
            unique -= 1
        left += 1
    if right - left + 1 > best_length:  #current window is valid
        best_length = right - left + 1
        best_left = left
        best_right = right
print(best_left + 1, best_right + 1)  #1-based idx
