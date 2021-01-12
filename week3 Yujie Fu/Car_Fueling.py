import sys

data = list(map(int,sys.stdin.read().split()))
d = data[0]
m = data[1]
n = data[2]
stops = data[3:]
stops = [0]+stops+[d]
current = 0
temp_d = 0
which_add = 0
add_time = 0
a = True
for i,j in enumerate(stops):
    if j == d:
        if j - current > m:
            a = False
            continue
        continue
    if j == 0:
        continue
    if which_add > i-1:
        continue
    count = 0
    while stops[i] - current <= m:
        count = 1
        i = i + 1
        if i >= n+2:
            break
    current = stops[i-1]
    if count == 0:
        a = False
        if j == d:
            a = True
        break
    which_add = i-1
    add_time += 1
if a:
    if d>m:
        print(add_time)
    else:
        print(0)
else:
    print(-1)
    

            
            
    
    
