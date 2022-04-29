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

pais_elegido = input("ingrese pais para buscar sus tipo de shows: ")

conj_show = set()
todos_paises = set()

#------------------------------OBTENER SHOW DEL PAIS INGRESADO----------------------------------------------------

#verifica si el pais elegido esta en la lista de "country"
def encontre_pais(str_paises, pais_elegido) -> bool:
    return True if pais_elegido in (str_paises.split(",")) else False;

#obtiene el type_show del pais ingresado
def obtener_show(lis_paises, show, pais_elegido) -> set:
    return [show for country in lis_paises if encontre_pais(country, pais_elegido)]

#-----------------------------OBTENER TODOS LOS PAISES---------------------------------------------------------------------
#agrega paises a lis_paises sin repeticion
def encontrar_paises(lis_paises) -> set:

    return set(map(lambda x: lis_paises.append(x), str(lis_paises).split(",")))

#--------------------Realizar una función que dado un país informe si es parte de la línea del show pasado como argumento-----

def

for elem in datos:
    conj_show = obtener_show(elem[pos_country], elem[pos_type], pais_elegido)
    todos_paises = encontrar_paises(elem[pos_country])
    informar_si_es_parte()
