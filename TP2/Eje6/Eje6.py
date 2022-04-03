frase = """Si trabajás mucho CON computadoras, eventualmente encontrarás que te gustaría
automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y
reemplazo en un gran número DE archivos de texto, o renombrar y reorganizar
un montón de archivos con fotos de una manera compleja. Tal vez quieras
escribir alguna pequeña base de datos personalizada, o una aplicación
especializada con interfaz gráfica, o UN juego simple."""
#elimino saltos de linea, comas y puntos y armo lista con las palabras
frase = frase.replace("\n", " ").replace(".", "").replace(",", "")

frase_list = frase.lower().split(" ")

lis_sin_rep = list(filter(lambda x: frase.count(x) == 1, frase_list))

print(lis_sin_rep)