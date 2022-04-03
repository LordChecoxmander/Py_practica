cadena = input("Ingresa la clave (debe tener menos de 10 caracteres y no contener los símbolos:@ y !):")

if len(cadena) > 10:
    print("Ingresaste más de 10 carcateres")

#cuanto las ocurrecias de @ y !
"""cant = 0
for car in cadena:
    if car == "@" or car == "!":
        cant = cant + 1                
if cant >= 1:
    print("Ingresaste alguno de estos símbolos: @ o !" )
else:
    print("Clave válida")"""

print("Ingresaste alguno de estos símbolos: @ o !") if (cadena.count("@") + cadena.count("!")) > 0 else print("Clave válida")
