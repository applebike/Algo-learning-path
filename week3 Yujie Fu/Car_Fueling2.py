import sys

data = list(map(int,sys.stdin.read().split()))
d = data[0]
m = data[1]
n = data[2]
stops = data[3:]


position = 0
p_mile = 0
add_time = 0
a = True

for i, j in enumerate(stops):
    if position != i:
        continue
    add_time = add_time + 1
    count = 0
    while stops[i] - p_mile <= m:
        count = 1       
        i = i+1
        if i == n:
            break
    
    
    if count == 0:
        a = False
        break
    
    if i == n:
        break
    position = i
    p_mile = stops[i-1]

if m - d >= 0:
    print(0)
elif a == False:
    print(-1)
elif d - stops[-1] > m:
    print(-1)
else:
    print(add_time)
        
