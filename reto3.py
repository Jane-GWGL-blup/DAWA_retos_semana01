#Reto3 Invertiendo cadenas

txt=input("Ingrese algún texto:\n")

def invertir_cadena(cadena):
    cadena_invertida=""
    for i in cadena:
        cadena_invertida=i+cadena_invertida
    return cadena_invertida

print(invertir_cadena(txt))