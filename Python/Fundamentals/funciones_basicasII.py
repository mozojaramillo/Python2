#Cuenta regresiva
def cuenta_regresiva(a):
    lista =[]
    for i in range(a,-1,-1):
        lista.append(i)
    return lista

print(cuenta_regresiva(5))

def lista_de_dos(lista):
    print(lista[0])
    return(lista[1])
c = lista_de_dos([1,2])
print(c)

def first_plus_length(lista):
    return lista[0] + len(lista)
print(first_plus_length([1,2,3,4,5]))

def values_greater_than_second(lista):
    
    largo = len(lista)
    lista2 =[]

    if largo < 2:
        return False

    for i in lista:
        if i>lista[1]:
            lista2.append(i)
    print('El largo de la nueva lista es', len(lista2))
    return lista2

test = [5]
print(values_greater_than_second(test))

def length_and_value(a,b):
    lista=[]
    for i in range(0,a):
        lista.append(b)
    return lista

print(length_and_value(4,7))