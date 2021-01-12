import sys

#read data
def compare(a,b):
    if a+b > b+a:
        return a
    else:
        return b

data = list(sys.stdin.read().split())
n = int(data[0])
numbers = data[1:]
final_num = ''
while len(numbers) > 0:
    better = numbers[0]
    for num in numbers:
        better = compare(better, num)
    final_num += better
    numbers.remove(better)
print(final_num)
    
