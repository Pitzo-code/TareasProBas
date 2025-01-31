#problema 9
limit = 1010

par= []
impar = list()

for num in range(1,limit+1):
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

tamanio = max(len(par),len(impar))

for item in range(tamanio):
    try:
        print(impar[item], par[item],)
    