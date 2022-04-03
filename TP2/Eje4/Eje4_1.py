evaluar = """ título: Experiences in Developing a Distributed Agent-based Modeling Toolkit
with Python
resumen: Distributed agent-based modeling (ABM) on high-performance computing resources
provides the promise of capturing unprecedented details of large-scale complex systems.
However, the specialized knowledge required for developing such ABMs creates barriers to
wider adoption and utilization. Here we present our experiences in developing an initial
implementation of Repast4Py, a Python-based distributed ABM toolkit. We build on our
experiences in developing ABM toolkits, including Repast for High Performance Computing
(Repast HPC), to identify the key elements of a useful distributed ABM toolkit. We leverage
the Numba, NumPy, and PyTorch packages and the Python C-API to create a scalable modeling
system that can exploit the largest HPC resources and emerging computing architectures.
"""

#reemplazo los saltos de linea por espacios
evaluar_2 = evaluar.replace("\n", "")

# divido evaluar en "resumen:" y casteo a str
str_tit, str_res = evaluar_2.split("resumen: ")

print(str_tit)
#divido str_res por oraciones(str_tit no es necesario xq es solo una oracion"
#lis_resumen = str_res.split(".")
# elimino el "titulo:" de la lista y genero las listas de ambos str
lis_titulo = str(str_tit).split(" ")
del lis_titulo[0:2]
#evaluo palabras del titulo
print("titulo ok") if len(lis_titulo) <= 10 else print("titulo !ok")

"""print(str_res)
print(type(str_res))"""
lis_resumen = str(str_res).split(".")
"""print(lis_resumen[0])
lis_resumen = filter(str(lis_resumen).split(" "), lis_resumen)
print("1")
print(lis_resumen[0])"""
#print(lis_resumen[0])
#print(len(lis_resumen))
#evaluo la lista por sus longitudes(palabras)
#for elem in filter(lambda x: len(lis_resumen), lis_resumen):

for ind in range(len(lis_resumen)):

    sub_lis = lis_resumen[ind].split(" ")
    #print(sub_lis)
    match sub_lis:
        case sub_lis if len(sub_lis) < 13:
            print("facil de leer")
        case sub_lis if 12 < len(sub_lis) < 18:
            print("aceptable de leer")
        case sub_lis if 17 < len(sub_lis) < 26:
            print("dicifil de leer")
        case sub_lis if 25 < len(sub_lis):
            print("muy dificil")

"""case > 25 :
            print("muy dificil ")"""

"""match filter(lambda x: len(lis_resumen), lis_resumen):
    case x if x < 13:
        print("facil de leer")
    case x if 13 <= x <= 17:
        print("aceptable de leer")
    case x if 18 <= x <= 25:
        print("aceptable de leer")
    case x if x > 25:
        print("aceptable de leer")"""