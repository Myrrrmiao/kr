a = int(input())
b = int(input())
c = int(input())
d = int(input())

table = ''

for i in range(c, d + 1):
    table = table + '\t' + str(i)

for line in range(a, b + 1):
    table = table + '\n' + str(line)
    for column in range (c, d + 1):
        result = line * column
        table = table + '\t' + str(result)

print(table)