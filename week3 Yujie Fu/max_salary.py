import sys


#read data

data = list(map(int, sys.stdin.read().split()))
n = data[0]
numbers = data[1:]
n_1000 = 0
if 1000 in numbers:
    n_1000 = numbers.count(1000)
    
numbers_ind = []
final_num = ''
for i in range(n):
    numbers_ind.append((i, numbers[i]))

#print(numbers_ind)

digit = 9
while digit > 0:
    sub_numbers_ind = []
    for num in numbers_ind:
        fd = int(str(num[1])[0])
        #print(fd)
        if fd == digit:
            sub_numbers_ind.append(num)
    #print(sub_numbers_ind)
    new_sub = []
    for num in sub_numbers_ind:
        tup = ()
        if len(str(num[1])) == 3:
            tup = (num[0], num[1], num[1])        
        if len(str(num[1])) == 2:
            tup = (num[0],int(str(num[1])+str(digit)) - 0.01,num[1])
        if len(str(num[1])) == 1:
            tup = (num[0],int(str(num[1])+2*str(digit)),num[1])
        if len(str(num[1])) == 4:
            continue
        new_sub.append(tup)
    #print(new_sub)
    new_sub = sorted(new_sub, key = lambda x: x[1], reverse = True)
    #print(new_sub)
    for num in new_sub:
        final_num += str(num[2])
        
            
            
        



        
    #
    #print(digit)
    digit = digit - 1

print(final_num + '1000'*n_1000)
