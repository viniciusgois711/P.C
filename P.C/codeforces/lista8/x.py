def encontrar_senha(qtd, niveis_oleosidade):
    # Cria uma lista de pares (oleosidade, digito)
    digitos_com_oleosidade = [(niveis_oleosidade[i], i) for i in range(10)]
    
    # Ordena a lista por oleosidade em ordem decrescente e, em caso de empate, por dígito em ordem crescente
    digitos_com_oleosidade.sort(key=lambda x: (-x[0], x[1]))
    
    # Gera a senha com os N primeiros dígitos
    senha = ''.join(str(digito) for _, digito in digitos_com_oleosidade[:qtd])
    
    return senha

# Armazena o resultado para cada caso
resultado = []
caso = 1

while True:
    try:
        # Lê a quantidade de dígitos da senha
        qtd = int(input())
        
        # Lê os níveis de oleosidade
        niveis_oleosidade = list(map(float, input().split()))
        
        # Encontra a senha
        senha = encontrar_senha(qtd, niveis_oleosidade)
        
        # Armazena o resultado no formato especificado
        resultado.append(f"Caso {caso}: {senha}")
        caso += 1
        
    except EOFError:
        break

# Imprime todos os resultados
for res in resultado:
    print(res)
