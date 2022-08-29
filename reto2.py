#Reto2 EL FAMOSO "FIZZBUZZ"

num = int(input("Ingrese un numero de 1 al 100: "))
if num >= 1 & num <= 100:
    if num%3==0 & num%5==0:
        print("fizzbuzz")
    elif num%3==0:
        print("fizz")
    elif num%5==0:
        print("buzz")
    else:
        print(num)
else:
    print("Número fuera del rango establecido") 




