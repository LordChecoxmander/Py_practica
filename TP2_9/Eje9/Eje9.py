celdas = ['-*-*-', '--*--', '----*', '*----']

#copio lista a modificar
celdas_2 = celdas.copy()

print(celdas[1][2])
#evaluo si el lugar tiene una mina o no
def is_mina(lugar):
    return True if (lugar == "*") else False

#cambia el - por el numero de minas cercanas
def cambiar_celda():
    return 1


#itera el str, devolviedno el modificado
def devolver_numero(lugar) :
    if is_mina(lugar):
        cambiar_celda()


celdas_2 = celdas.copy()
print(celdas_2)
#itera el str, devolviedno el modificado
celda_final = filter(filter(devolver_numero(x), celdas_2))


