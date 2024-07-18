def inverter_r(s):
    qtd = len(s)
    if qtd == 0:
        return ""

    nova = s[1:]
    nova_r = inverter_r(nova)
    nova_r += s[0]

    return nova_r

def inverter(s):

    invertido = inverter_r(s)

    if invertido == s:
        return True
    else:
        return False

s = "abab"

print(inverter(s))
