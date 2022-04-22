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

#obtengo el numero de la posicin country en el header
num_country = header.index("country")
#print(num_country)

#pais = input("ingrese pais para buscar sus tipo de shows: ")

#print(list(data_net[5]))

#agrega paises a lis_paises sin repeticion
def encontrar_paises(lis_paises) -> set:

    return map(lambda x:  ,str(lis_paises).split(","))



def trabajar_lista(x, num_country, tipo_show, todos_paises):

    todos_paises = encontrar_paises(x[num_country])





tipo_show = []
todos_paises = set()

list_pai = map(lambda x: trabajar_lista(x, num_country, tipo_show, todos_paises), datos)
