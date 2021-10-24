def ordenar(lista):
    for j in range(0,len(lista)-1):
        for i in range(0, len(lista)-1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
    print(lista)

x = [6,5,4,3,2,1]

print(ordenar(x))
