

#apertura de archivos
arch_nom = open('nombres_1.txt', "r", encoding="utf8")
arch_eval1 = open('eval1.txt', 'r')
arch_eval2 = open('eval2.txt', 'r')

#uso readlines para saber el tamaño del archivo y despues vuelvo a poner el puntero en la posicion inicial
tamano= len(arch_nom.readlines())
arch_nom.seek(0)

#creo una lista de tuplas con nombre y promedio
lista_alum = [
                (str(arch_nom.readline()).replace(",", "").replace("\n", "").replace(" '", "").replace("'", ""),
                (int(arch_eval1.readline().replace(",", "")) + int(arch_eval2.readline().replace(",", "")))/2)
                for ind in range(tamano)
              ]

#cierre de archivos
arch_nom.close()
arch_eval1.close()
arch_eval2.close()

#itero lista para obtener promedio_general
prom_general = 0
for i in range(len(lista_alum)):
    prom_general += lista_alum[i][1]
prom_general /= len(lista_alum)
print(f"Promedio general: {prom_general}")

#itero lista para obtener lista de los alumnos por debajo del promedio general
lista_alum_mayor = list(filter(lambda x: x[1] < prom_general, lista_alum))
print(f"lista de alumnos con calificacion menos al promedio: {lista_alum_mayor}")