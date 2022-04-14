#abro archivos de nombres
from heapq import merge

nombres1 = open('nombres_1.txt', "r", encoding="utf8")
nombres2 = open('nombres_2.txt', "r", encoding="utf8")

#creo listas usanto  list comprehension
list_nombres1 = [x.replace(" '", "").replace("',\n", ""). replace("'", "").title()
                    for x in nombres1]

list_nombres2 = [x.replace(" '", "").replace("',\n", "").title()
                    for x in nombres2]

#aplico un merge con las 2 listas, un setr para eliminar elementos repetidos y para ordenarlos con un sort lo convierto a lista
merge = sorted(list(set(merge(list_nombres1, list_nombres2))))
print(f'nombres en ambos archivos: {merge}')

#abro archivo de notas
notas1 = open("eval1.txt", "r")
notas2 = open("eval2.txt", "r")

#creo listas de notas
list_notas1 = [x.replace(",\n", "").replace(" ", "")
               for x in notas1]
list_notas2 = [x.replace(",\n", "").replace(" ", "")
               for x in notas2]

#cierro archivos
nombres1.close()
nombres2.close()
notas2.close()
notas1.close()

#imprimo con formato de la imagen
formato1 = "{:2} {:16} {:10} {:10} {:10}"
print(formato1.format(" ", "Nombre", "Eval1", "Eval2", "Total"))
for i in range(len(list_nombres1)):
    print(formato1.format(i , list_nombres1[i], list_notas1[i], list_notas2[i], list_notas1[i] + list_notas2[i]))
















