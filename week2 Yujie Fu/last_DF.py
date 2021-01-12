n = int(input())

a = 1
b = 1
c = 0

if n == 0:
    print(0)
elif n == 1 or n == 2:
    print(1)
else:
    for i in range(n-2):
        c = (a+b)%10
        a = b
        b = c
    print(c)
