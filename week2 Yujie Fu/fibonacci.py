n = int(input())


if n == 1 or n == 2:
    print(1)
elif n == 0:
    print(0)
else:
    fibo = [1,1]
    for i in range(n-2):
        fibo.append(fibo[i]+fibo[i+1])
    print(fibo[-1])
        
    
