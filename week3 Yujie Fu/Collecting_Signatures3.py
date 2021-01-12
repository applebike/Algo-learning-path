import sys

data = list(map(int, sys.stdin.read().split()))

n = data[0]
a_list = []
current = 1

#没读完就一直读取数据, read data
while current < (2*n):
    sub_list = []
    sub_list.append(data[current])
    current = current + 1
    sub_list.append(data[current])
    current = current + 1
    a_list.append(sub_list)

# find all optimal points

points = []
a_list = sorted(a_list, key = lambda x: x[1])
current = a_list[0][1]

points.append(a_list[0][1])
for i in a_list:
    if (current <i[0]) :
        
        current = i[1]
        
        points.append(current)
print(len(points))
for i in points:
    print(i, end = ' ')
        
