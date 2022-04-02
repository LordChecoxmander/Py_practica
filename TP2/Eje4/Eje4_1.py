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
# divido evaluar en "resumen:"
evaluar.replace("\n"," ")

#if evaluar.__contains__("\n"):
evaluar_2 = evaluar.replace("\n", " ")

str_tit, str_res = evaluar.split("resumen: ")
print(evaluar_2)
#divido str_res por oraciones(str_tit no es necesario xq es solo una oracion"
#lis_resumen = str_res.split(".")
# elimino el "titulo:" de la lista y genero las listas de ambos str
lis_titulo = str(str_tit.split(".")).split(" ")
lis_resumen = str(str_res.split(".")).split(" ")
del lis_titulo[0:2]

#elimino \n

#lis_titulo = list(filter(lambda c: c.remove("\\n"), lis_titulo))
#print(lis_titulo)
