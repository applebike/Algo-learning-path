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
    
a = 0
# while loop data manipulation
while True:
    a += 1
    new_list = a_list[0]
    ind = []
    for i in range(len(a_list)):
        if new_list[1] <= a_list[i][1] and new_list[1] >= a_list[i][0]:
            if new_list[0] <= a_list[i][0]:               
                new_list = [a_list[i][0], new_list[1]]
            else:
                new_list = new_list
            ind.append(i)
            continue

            
        if a_list[i][1] <= new_list[1] and a_list[i][1] >= new_list[0]:
            if a_list[i][0] <= new_list[0]:
                new_list = [new_list[0], a_list[i][1]]
            else:
                new_list = a_list[i]
            ind.append(i)
            
    new_a = []
    for i in range(len(a_list)):
        if i not in ind:
            new_a.append(a_list[i])
        
    new_a.append(new_list)
    if len(ind) == 1 and a > n+1000:
        break
    a_list = new_a
    
    

# print result
print(len(a_list))
for i in a_list:
    if i != a_list[len(a_list) - 1]:
        print(i[0], end = ' ')
    else:
        print(i[0])



