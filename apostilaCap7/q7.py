def av1(a1,a2,a3):
    l = [a1,a2,a3]
    l_ordenado = sorted(l)
    return (l_ordenado[1]+l_ordenado[2])/2

def nota1(l,a):
    avaliacoes = a/2
    lista = l/2
    return avaliacoes+lista

def av2(a1,a2,a3,a4,a5):
    l = [a1,a2,a3,a4,a5]
    l_ord = sorted(l)
    return (l_ord[1]+l_ord[2]+l_ord[3])/3

def nota2(l,a):
    avaliacoes = a*0.8
    lista = l*0.2
    return avaliacoes+lista

def notaFinal(nota1, nota2):
    media = (nota1*2+nota2*3)/5
    if media>=60:
        return "APROVADO"
    else: return "NAO APROVADO"

l1, a11, a21, a31 = map(int,input().split())
l2, a12, a22, a32, a42, a52 = map(int,input().split())

n1 = nota1(l1,av1(a11,a21,a31))
n2 = nota2(l2,av2(a12,a22,a32,a42,a52))

print(notaFinal(n1,n2))
