def grande(lista):
    for i in range(0,len(lista)):
        if lista[i] > 0:
            lista[i] = "grande"
    return lista
alfa = [-1,3,5,-5]

print(grande(alfa))

def positives(lista):
    contador = 0
    for i in lista:
        if i > 0:
            contador = contador + 1
    lista[-1] = contador
    return lista

print(positives([-1,1,1,1]))

def suma_total(lista):
    suma = 0
    for i in lista:
        suma = suma + i
    return suma

print(suma_total([1,2,3,4]))

def promedio(lista):
    prom = suma_total(lista)/len(lista)
    return prom

print(promedio([1,2,3,4]))

def long(lista):
    largo = 0
    for i in lista:
        largo = largo + 1
    return largo
print(long([1]))

def minimo(lista):
    if len(lista) == 0:
        return False
    min = lista[0]
    for i in lista:
        if i < min:
            min = i
    return min

print(minimo([37,2,1,-9]))

def maximo(lista):
    if len(lista) == 0:
        return False
    max = lista[0]
    for i in lista:
        if i > max:
            max = i
    return max

print(maximo([37,2,1,-9]))

def analisis(lista):
    Datos = ["suma", "promedio", "minimo", "maximo", "longitud"]
    funciones = [suma_total(lista),promedio(lista),minimo(lista),maximo(lista), len(lista)]
    resumen = {}
    for i,j in zip(Datos,funciones):
        resumen[i]= j
    return resumen

print(analisis([37,2,1,-9]))

def inversa(lista):
    a = len(lista)
    for i in range(a-1,-1,-1):
        lista.append(lista[i])
    print(lista)
    for j in range(0,a):
        lista.pop(0)
    return (lista)

print(inversa([37,2,1,-9]))
