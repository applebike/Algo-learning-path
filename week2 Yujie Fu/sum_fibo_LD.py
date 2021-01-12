
n = int(input())%60

a = 1
b = 1
s = 2
if n == 0:
    print(0)
elif n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    for i in range(n-2):
        a,b = b,(a+b)%10
        s += b
        s = s%10
    print(s)
    
    

