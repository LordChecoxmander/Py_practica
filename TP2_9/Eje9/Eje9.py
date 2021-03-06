

# verifica si la posicin es valida para contar a ambos lados
# y cuento minas cercanas
def verificar_char_2(num_lin, num_char, celdas):
    n = 0
    if (num_char >= 1) and is_mina(celdas[num_lin][num_char - 1]):  # si no entra estoy en la linea 1
        n += 1

    if (num_char < len(celdas[num_lin])) and (is_mina(celdas[num_lin][num_char + 1])):  # si no es la ultima linea
        n += 1

    return n


# verifica si la posicin es valida para contar a ambos lados
# y cuento minas cercanas
def verificar_char(num_lin, num_char, celdas):
    n = 0
    if (num_char >= 1) and is_mina(celdas[num_lin][num_char - 1]):  # si no entra estoy en la linea 1
        n += 1

    if is_mina(celdas[num_lin][num_char]):
        n += 1

    if (num_char < len(celdas[num_lin])):
        if (is_mina(celdas[num_lin][num_char + 1])):  # si no es la ultima linea
            n += 1

    return n


# verifica si las lineas son validas para contar
# y realizo cambio en celdas_2
def verificar_linea(num_lin, num_char, celdas_2, celdas):
    numero = 0
    if num_lin >= 1:  # si no entra estoy en la linea 1
        numero += verificar_char(num_lin - 1, num_char, celdas)

    numero += verificar_char_2(num_lin, num_char, celdas)  # solo veridica el char a los costados y suma

    if num_lin < len(celdas):  # si no es la ultima linea
        numero += verificar_char(num_lin + 1, num_char, celdas)

    celdas_2[num_lin][num_char] = chr(numero)


# evaluo si el lugar tiene una mina o no,
# retorna True si hay
def is_mina(letra):
    return True if (letra == "*") else False


celdas = ['-*-*-', '--*--', '----*', '*----']
# copio celdas a modificar
celdas_2 = celdas.copy()

# celdas_2 = list(filter(lambda x: list(x), celdas_2))
for indice in range(len(celdas_2)):
    celdas_2[indice] = list(celdas_2[indice])
print(len(celdas_2[2]))

# 1º filter itera cada strs de la list celdas
# 2º filter itera cada char del str(enviado por el prmer filter)
# celda_final = filter(lambda x: filter(lambda c: devolver_numero(c, celdas, celdas_2), x), celdas)
num_lin = 0
for linea in celdas:

    num_letra = 0
    for letra in linea:
        if not is_mina(letra):
            verificar_linea(num_lin, num_letra, celdas_2, celdas)  # envia la posicion del - en la lista como parametro
        num_letra += 1

    num_letra += 1

print(celdas_2)
