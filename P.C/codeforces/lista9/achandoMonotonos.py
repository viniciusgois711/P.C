qtd = int(input())
texto = input()

vezes = resultado = 0

for x in range(0, qtd):
    if texto[x] == 'a':
        vezes += 1
    
    if texto[x] == 'b' and vezes == 1:
        vezes = 0
    elif texto[x] == 'b':
        resultado += vezes
        vezes = 0

if vezes>1:
    resultado += vezes

print(resultado)