def soma(x):
    if x < 10:
        return x
    somar = x%10 + soma(x//10)
    return somar 

s = int(input())
a = int(input())
b = int(input())

menor = maior = 0
digito = []

for x in range(a, b+1):
    if soma(x) == s:
        digito.append(x)

digito.sort()

qtd = len(digito)

print(digito[0])
print(digito[qtd-1])