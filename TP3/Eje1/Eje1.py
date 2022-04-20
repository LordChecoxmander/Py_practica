path_files = "files"
archivo_net = "netflix_titles.csv"

import csv
#import os.path
import os

path_files = "files"
archivo_net = "netflix_titles.csv"
path_arch = os.path.join(os.getcwd(), path_files)

archivo = open(os.path.join(path_arch, archivo_net), "r", encoding="utf-8")
#archivo = open("netflix_titles.csv", "r", encoding="utf-8")
data_net = csv.reader(archivo, delimiter=',')
header, datos = next(data_net), list(data_net)


#pais = input("ingrese pasi a buscar: ")

#print(list(data_net[5]))
#def is_country(x) -> bool:

#    return

for linea in datos:
    print(linea)



list_pai = map(lambda x: is_country(x), )
