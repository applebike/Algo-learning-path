# Uses python3
def calc_fib(n):
    if n == 1 or n == 2:
        return 1
    elif n == 0:
        return 0
    else:
        fibo = [1,1]
        for i in range(n-2):
            fibo.append(fibo[i]+fibo[i+1])
        return fibo[-1]
        
  

        
numbers = input()
n,m = numbers.strip().split()
n = int(n)
m = int(m)


list1 = []
count = 0
a = True
while a:
    list1.append(calc_fib(count)%m)    
    if count == 0 or count == 1:
        count = count + 1
        continue
    count = count + 1
    if list1[count-2] == 0 and list1[count-1] == 1:
        break
list1 = list1[:len(list1)-2]
length = len(list1)
mod = n%length


print(list1[mod])

    
    





