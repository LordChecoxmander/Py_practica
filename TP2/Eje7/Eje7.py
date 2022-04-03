#palablra =  input("ingrese una palabra: ")
palabra = "Portón"

#elimino espacios
pal_list = list(palabra.replace(" ", "").lower())
print(pal_list)
bool = False

"""def es_heterograma(pal_lis, x):

    if(pal_lis.find(x) > 1):
        bool = True

lis = filter(es_heterograma(pal_list, ), pal_list)"""

for elem in pal_list:

    if pal_list.count(elem) > 1:
        bool = True


print("es heterograma") if not bool else print(" ! heterograma")