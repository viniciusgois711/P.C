




# somar os digitos
somar = 0
def soma(x):
    if x < 10:
        return x

    somar += x%10 + soma(x/10)

    return somar 


print(soma(234))