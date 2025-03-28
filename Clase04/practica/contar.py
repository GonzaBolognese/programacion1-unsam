data = [4, 9, 1, 25, 16, 100, 49]

print(min(data))
print(max(data))
print(sum(data))
print('------------------------')

for x in data:
    print(x)

print('------------------------')

for n, x in enumerate(data):
    print(n,x)

print('------------------------')

for n in range(len(data)-1):
    print(data[n])