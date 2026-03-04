import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

left, curr_sum, count = 0,0,0 

for right in range(0, n):
    curr_sum += arr[right]
    while curr_sum > s:
        curr_sum -= arr[left]
        left += 1
    count += right - left + 1

print(count)
