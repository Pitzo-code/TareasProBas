#problema 24
print("¿que tipo de suma es?")
print("1.Suma Aritmetica")
print("2.suma geometrica")
print('3.Ambas')

elec = int(input("ingrese el numero de la opcion deseada: "))

if elec ==1:
    PrmTerm= int(input("ingrese el primer numero: "))
    UltTerm= int(input("ingrese el ultimo  numero: "))
    nTerm= int(input("ingrese el numero de terminos: "))
    Sumatoria= ((PrmTerm + UltTerm) * nTerm)/21
    print('La sumatoria es de: ',Sumatoria)
elif elec ==2:
    PrmTerm= int(input("ingrese el primer numero: "))
    Raz= int(input("ingrese el la razon comun: "))
    nTerm= int(input("ingrese el numero de terminos: "))
    Sumatoria= PrmTerm * (1 - Raz**nTerm)/(1-Raz)
    print('La sumatoria es de: ',Sumatoria)
elif elec == 3:
    PrmTerm= int(input("ingrese el primer numero: "))
    UltTerm= int(input("ingrese el ultimo  numero: "))
    nTerm= int(input("ingrese el numero de terminos: "))
    Aritmetica= ((PrmTerm + UltTerm) * nTerm)/2
    Raz= int(input("ingrese el la razon comun: "))
    geometrica= PrmTerm * (1 - Raz**nTerm)/(1-Raz)
    print('La sumatoria aritmetica es de: ',Aritmetica)
    print('La sumatoria geometrica es de: ',geometrica)
