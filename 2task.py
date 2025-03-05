a = int(input('Человек в команде биологов = '))
b = int(input('Человек в команде информатиков = '))

def gcd (a, b, step=0):
    print(step)
    if a == 0 or b == 0:
        return a + b
    if a > b:
        return gcd (a - b, b, step + 1)
    else:
        return gcd (a, b - a, step + 1)

product = a * b

nod = gcd (a, b)
nok = product // nod

print (nok)
