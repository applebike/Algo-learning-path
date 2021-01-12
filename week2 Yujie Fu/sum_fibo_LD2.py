n1,n2 = input().strip().split()

n1 = int(n1)%60 - 1
n2 = int(n2)%60


def calculate_s1(n1):
    a,b,s = 1,1,2
    if n1 == 0 or n1 == -1:
        return a,b,0
    elif n1 == 1:
        return a,b,1
    elif n1 == 2:
        return a,b,2
    else:
        for i in range(n1-2):
            a,b = b,(a+b)%10
            s += b
            s = s%10
        return a,b,s
    
def calculate_s2(n2):
    a,b,s = 1,1,2
    if n2 == 0:
        return 0
    elif n2 == 1:
        return 1
    elif n2 == 2:
        return 2
    else:
        for i in range(n2 - 2):
            a,b = b,(a+b)%10
            s += b
            s = s%10
        return s





a,b,s1 = calculate_s1(n1)
s2 = calculate_s2(n2)

if s2-s1 < 0:
    print(s2+10-s1)
else:
    print(s2-s1)






            
    
