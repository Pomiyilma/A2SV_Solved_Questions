import sys
input = sys.stdin.readline
 
MAXT = 200000
 
n, k, q = map(int, input().split())
diff = [0] * (MAXT + 2)  #diff=[0,0,0.....]
 
for _ in range(n):
    l, r = map(int, input().split())
    diff[l] += 1  #diff[l]= diff[l] + 1
    diff[r + 1] -= 1 #diff[r+1]=diff[r+1] - 1
coverage = [0] * (MAXT + 1) #coverage=[0,0,...]
curr = 0
for t in range(1, MAXT + 1):
    curr += diff[t]
    coverage[t] = curr
 
good = [0] * (MAXT + 1)
for t in range(1, MAXT + 1):
    if coverage[t] >= k:  #admitted
        good[t] = 1
pref = [0] * (MAXT + 1)
for t in range(1, MAXT + 1):
    pref[t] = pref[t - 1] + good[t]
 
for _ in range(q):
    a, b = map(int, input().split())
    print(pref[b] - pref[a - 1])
