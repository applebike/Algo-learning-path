import sys

data = list(map(int, sys.stdin.read().split()))
n = data[0]
upper_s = data[1:n+1]
lower_s = data[n+1: ]

revenue = 0
s1_p = []
s1_n = []
for i in upper_s:
    if i < 0:
        s1_n.append(i)
    else:
        s1_p.append(i)

s2_p = []
s2_n = []
for i in lower_s:
    if i < 0:
        s2_n.append(i)
    else:
        s2_p.append(i)

s1_count_p = len(s1_p)
s2_count_p = len(s2_p)

s1_p.sort()
s2_p.sort()
s1_p.reverse()
s2_p.reverse()

s1_n.sort()
s2_n.sort()

double_p = min(s1_count_p, s2_count_p)
double_n = min(len(s1_n), len(s2_n))

for i in range(double_p):
    revenue += s1_p[i] * s2_p[i]

for i in range(double_n):
    revenue += s1_n[i] * s2_n[i]

for i in range(abs(s1_count_p - s2_count_p)):
    if s1_count_p - s2_count_p > 0:
        revenue += s1_p[double_p+i]*s2_n[-(i+1)]
    if s1_count_p - s2_count_p < 0:
        revenue += s2_p[double_p+i]*s1_n[-(i+1)]

print(revenue)


