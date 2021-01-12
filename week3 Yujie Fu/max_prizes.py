
#read data
n = int(input())
current = 1
opt = []
while n > 0:
    if n - current > current:
        opt.append(current)
        n = n - current
        current = current + 1
    else:
        opt.append(n)
        n = 0
print(len(opt))
for i in opt:
    print(i, end = ' ')
        
    
