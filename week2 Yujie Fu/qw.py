a = int(input())
b = [int(i) for i in input().split()]
b.append(a)

max1 = max(b)
b.remove(max1)

max2 = max(b)

print(max1*max2)
