numbers = input().strip().split()
a = int(numbers[0])
b = int(numbers[1])
a1 = a
b1 = b
c = 1

while c == 1:
    if a == b or a ==0 or b ==0:
        c = 0      
    elif a > b:
        a = a%b       
    else:
        b = b%a
if a == 0 or a == b:
    gcd = b
else:
    gcd = a


print(a1*b1//gcd)
