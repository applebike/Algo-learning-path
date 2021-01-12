import sys

data = list(map(int,sys.stdin.read().split()))
d = data[0]
m = data[1]
n = data[2]
stops = data[3:]
stops.append(d)
stops.append(0)
stops = [0] + stops
n = n + 1

a = 0

fill_num = 0
current = 0
#到终点不执行
while current < n:
    lastfill = current
    #如果超出终点不执行，油不够加 不执行
    while (current <= n and stops[current+1] - stops[lastfill] <= m):
        current += 1
        #print(current)
        

        

    if current == lastfill:
        a = 1
        print(-1)
        break
    #如果在终点，不加
    if current < n :
        #print('c')
        fill_num += 1
if a != 1:
    print(fill_num)
