with open('..\data\camion.csv', 'rt') as f:
    data = f.read()

print(data)

with open('..\data\camion.csv', 'rt') as f:
    for line in f:
        print(line, end='')

factos= open('..\data\camion.csv', 'rt')
headers= next(factos).split(',')
print(headers)

for line in factos:
    print(line.split(','))

factos.close()