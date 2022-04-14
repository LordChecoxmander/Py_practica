

#abro archivos de nombres
nombres1 = open('nombres_1.txt', "r", encoding="utf8")
nombres2 = open('nombres_2.txt', "r", encoding="utf8")

#creo listas usanto  list comprehension
list_nombres1 = [x.replace(" '", "").replace("',\n", "")
                    for x in nombres1]

list_nombres2 = [x.replace(" '", "").replace("',\n", "")
                    for x in nombres2]

def en_lista1(x):
    for i in list_nombres1:
        if i.lower() == x.lower(): return False
    return True

list_nombres1.extend([x for x in list_nombres2 if en_lista1(x)])

#list_nombres =[x for x in list_nombres2 if en_lista2(x)]




print(sorted(list_final))