import sys

data = list(map(int, sys.stdin.read().split()))
n,cap = data[0:2]
value = data[2:(2*n+2):2]
weight = data[3:(2*n+2):2]
unit_value = [value[i]/weight[i]  for i in range(len(value))]

fv = 0

while cap > 0:
    if len(value) == 0:
        break
    max_ind = unit_value.index(max(unit_value))
    if weight[max_ind] > cap:
        fv += cap/weight[max_ind] * value[max_ind]
        cap = 0
    elif weight[max_ind] <= cap:
        fv += value[max_ind]
        cap = cap - weight[max_ind]
        value.pop(max_ind)
        weight.pop(max_ind)
        unit_value.pop(max_ind)
    
print("{:.4f}".format(fv))
