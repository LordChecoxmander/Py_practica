path_files = "files"
archivo_net = "netflix_titles.csv"

import csv
#import os.path
import os

path_files = "files"
archivo_net = "netflix_titles.csv"
path_arch = os.path.join(os.getcwd(), path_files) #-> crea una direccion c:\blablabla\files

#abre el archivo "netflix.csv"(archivo_net) con la ruta c:\blablabla\files\netflix_titles.csv
archivo = open(os.path.join(path_arch, archivo_net), "r", encoding="utf-8")
data_net = csv.reader(archivo, delimiter=',')
header, datos = next(data_net), list(data_net)

#obtengo el numero de la posicion country en el header
pos_country = header.index("country")
pos_type = header.index("type")
print(header)

pais_elegido = input("ingrese pais para buscar sus tipo de shows: ")

#print(list(data_net[5]))

#agrega paises a lis_paises sin repeticion
def encontrar_paises(lis_paises) -> set:

    return set(map(lambda x: lis_paises.append(x), str(lis_paises).split(",")))

#verifica si el pais elegido esta en la lista de "country"
def encontre_pais(str_paises, pais_elegido) -> bool:

    return True if pais_elegido in (str_paises.split(",")) else False;


#verifico si el pais ingresado esta en la columna country, si esta se agrega a la lista tipo_show
def tipo_show_un_pais(lis_paises, pais_elegido, show_type) -> list:

    lis_show = [show_type for country in lis_paises if encontre_pais(country, pais_elegido)]
    for country in lis_paises:
        if encontre_pais(country, pais_elegido):
            lis_show.append(show_type)

    return
    #itero sobre la lista de "country" y envio el str a encontre_pais
    #return list(map(lambda x : encontre_pais(x, pais_elegido), lis_paises))

def trabajar_lista(x, pos_country, tipo_show, todos_paises, pais_elegido, pos_type):

    tipo_show = tipo_show_un_pais(x[pos_country], pais_elegido, x[pos_type])
    todos_paises = encontrar_paises(x[pos_country])





tipo_show = []
todos_paises = set()

list_pai = map(lambda x: trabajar_lista(x, pos_country, tipo_show, todos_paises, pais_elegido, pos_type), datos)
