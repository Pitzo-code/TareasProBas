#problema 21
import math

print("¿cual de las siguientes areas deseas calcular?")
print("1. Area del circulo")
print("2. Area del cuadrado")
print("3.area del triangulo")
print("4.area de rectangulo")

eleccion = int(input("ingrese el numero de la opcion deseada: "))

if eleccion==1:
    radio= float(input("ingrese el radio del circulo: "))
    area = math.pi*radio
    print("el área del circulo es de:",area)
elif eleccion==2:
    lado=float(input("ingrese la medda de un lado: "))
    area = lado**2
    print("el área del cuadrado es de:",area)
elif eleccion==3:
    base= float(input("ingrese la medida de la base: "))
    altura= float(input("ingrese la altura: "))
    area = (base * altura)/2
    print("el area del triangulo es: ",area)
elif eleccion == 4:
    baseMayor=float(input("ingrese la medida del lado mas grande: "))
    baseMenor=float(input("ingrese la medida del lado mas pequeño: "))
    area = baseMayor * baseMenor
    print("el area del rectangulo es: ",area)
else:
    print("opcion no valida")
